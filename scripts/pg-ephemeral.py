#!/usr/bin/env python3
"""
Ephemeral PostgreSQL server management without Docker.
Uses pinned postgresql-binaries (PostgreSQL 16.15.0) via uv.
Interface matches scripts/pg-ephemeral.sh:
  scripts/pg-ephemeral.py start -> prints DSN to stdout, 'container: NAME' to stderr
  scripts/pg-ephemeral.py stop NAME -> stops server and removes temp data
"""
import sys
import os
import shutil
import tempfile
import subprocess
import signal

PG_BINARIES_VERSION = "16.15.0"
DB_NAME = "postgres"
DB_USER = "postgres"

def get_base_tmp():
    base = os.path.join(tempfile.gettempdir(), "xq-luthor-pg")
    os.makedirs(base, exist_ok=True)
    return base

def start():
    import postgresql_binaries
    bindir = str(postgresql_binaries.bin())
    initdb = os.path.join(bindir, "initdb")
    pg_ctl = os.path.join(bindir, "pg_ctl")
    psql = os.path.join(bindir, "psql")

    # Generate a unique identifier/name for this instance
    pid = os.getpid()
    name = f"xq-luthor-pg-{pid}"
    inst_dir = os.path.join(get_base_tmp(), name)
    if os.path.exists(inst_dir):
        shutil.rmtree(inst_dir)
    os.makedirs(inst_dir, exist_ok=True)

    data_dir = os.path.join(inst_dir, "data")
    sock_dir = os.path.join(inst_dir, "sock")
    os.makedirs(sock_dir, exist_ok=True)

    # Pick a port: find an open port or use standard dynamic port
    import socket
    s = socket.socket()
    s.bind(('', 0))
    port = s.getsockname()[1]
    s.close()

    try:
        # Initialize cluster
        subprocess.check_call(
            [initdb, "-D", data_dir, "-E", "UTF8", "-A", "trust", "-U", DB_USER],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE
        )
        
        # Start cluster
        log_file = os.path.join(inst_dir, "pg.log")
        subprocess.check_call(
            [
                pg_ctl, "-D", data_dir, "-l", log_file,
                "-o", f"-k {sock_dir} -p {port} -h 127.0.0.1",
                "-w", "start"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.PIPE
        )

        # Apply schema.sql
        repo_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
        schema_path = os.path.join(repo_root, "database_schema", "schema.sql")
        if os.path.exists(schema_path):
            subprocess.check_call(
                [psql, "-h", "127.0.0.1", "-p", str(port), "-U", DB_USER, "-d", DB_NAME, "-v", "ON_ERROR_STOP=1", "-f", schema_path],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.PIPE
            )

        # Emit results
        print(f"postgresql://{DB_USER}:{DB_USER}@127.0.0.1:{port}/{DB_NAME}")
        sys.stderr.write(f"container: {name}\n")
        sys.stderr.flush()
    except Exception as e:
        # Cleanup on failure
        stop(name)
        sys.stderr.write(f"Error starting ephemeral postgres: {e}\n")
        sys.exit(1)

def stop(name):
    inst_dir = os.path.join(get_base_tmp(), name)
    if not os.path.exists(inst_dir):
        return
    data_dir = os.path.join(inst_dir, "data")
    try:
        import postgresql_binaries
        bindir = str(postgresql_binaries.bin())
        pg_ctl = os.path.join(bindir, "pg_ctl")
        if os.path.exists(data_dir):
            subprocess.call([pg_ctl, "-D", data_dir, "-m", "immediate", "-w", "stop"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except Exception:
        pass
    shutil.rmtree(inst_dir, ignore_errors=True)

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.stderr.write("Usage: pg-ephemeral.py start | stop NAME\n")
        sys.exit(2)
    cmd = sys.argv[1]
    if cmd == "start":
        start()
    elif cmd == "stop":
        if len(sys.argv) < 3:
            sys.stderr.write("Usage: pg-ephemeral.py stop NAME\n")
            sys.exit(2)
        stop(sys.argv[2])
    else:
        sys.stderr.write(f"Unknown command: {cmd}\n")
        sys.exit(2)
