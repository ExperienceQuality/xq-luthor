/**
 * Consumer sample for ADR 0002 nodejs clients (semver ≥ 1.2.0).
 * Intended for xq-mcp-style service tools once routine-service v1.2.0+ ships (#12).
 *
 * Not compiled in CI; illustrates the call shape reviewers asked for in GH issue #10.
 */
import {
  client,
  createRoutine,
  getRoutine,
  listRoutines,
} from "@experiencequality/routine-service-client";

client.setConfig({
  baseUrl: process.env.XQ_ROUTINE_BASE_URL ?? "http://localhost:8080",
  auth: () => process.env.XQ_JWT ?? "",
});

async function main() {
  const { data: page } = await listRoutines({ query: { limit: 20 } });
  console.log("routines", page?.items?.length ?? 0);

  const routineId = page?.items?.[0]?.routineId;
  if (!routineId) {
    return;
  }

  const { data: routine } = await getRoutine({ path: { routineId } });
  console.log("routine", routine?.routineId);

  const { data: created } = await createRoutine({
    body: {
      name: "Demo",
      exercises: [],
    },
  });
  console.log("created", created?.routineId);
}

void main();