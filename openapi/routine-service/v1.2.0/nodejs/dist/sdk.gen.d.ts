import { type Client, type ClientMeta, type Options as Options2, type RequestResult, type TDataShape } from './client';
import type { AddSessionErrors, AddSessionResponses, ArchiveRoutineErrors, ArchiveRoutineResponses, CaptureSnapshotErrors, CaptureSnapshotResponses, CreateRoutineErrors, CreateRoutineResponses, DeleteSessionErrors, DeleteSessionResponses, GetRoutineErrors, GetRoutineResponses, GetSessionErrors, GetSessionResponses, GetSnapshotErrors, GetSnapshotResponses, ListRoutinesErrors, ListRoutinesResponses, ListSessionExerciseRecordsErrors, ListSessionExerciseRecordsResponses, ListSnapshotsErrors, ListSnapshotsResponses, LivenessResponses, ReadinessResponses, ReplaceSessionErrors, ReplaceSessionResponses, RoutineCreate, RoutinePatch, SessionWrite, UpdateRoutineErrors, UpdateRoutineResponses } from './types.gen';
export type Options<TData extends TDataShape = TDataShape, ThrowOnError extends boolean = boolean, TResponse = unknown> = Options2<TData, ThrowOnError, TResponse> & {
    /**
     * You can provide a client instance returned by `createClient()` instead of
     * individual options. This might be also useful if you want to implement a
     * custom client.
     */
    client?: Client;
    /**
     * You can pass arbitrary values through the `meta` object. This can be
     * used to access values that aren't defined as part of the SDK function.
     */
    meta?: keyof ClientMeta extends never ? Record<string, unknown> : ClientMeta;
};
export declare const liveness: <ThrowOnError extends boolean = false>(options?: Options<never, ThrowOnError>) => RequestResult<LivenessResponses, unknown, ThrowOnError>;
export declare const readiness: <ThrowOnError extends boolean = false>(options?: Options<never, ThrowOnError>) => RequestResult<ReadinessResponses, unknown, ThrowOnError>;
export declare const listRoutines: <ThrowOnError extends boolean = false>(parameters?: {
    limit?: number;
    cursor?: string;
    includeArchived?: boolean;
}, options?: Options<never, ThrowOnError>) => RequestResult<ListRoutinesResponses, ListRoutinesErrors, ThrowOnError>;
export declare const createRoutine: <ThrowOnError extends boolean = false>(parameters: {
    routineCreate: RoutineCreate;
}, options?: Options<never, ThrowOnError>) => RequestResult<CreateRoutineResponses, CreateRoutineErrors, ThrowOnError>;
export declare const archiveRoutine: <ThrowOnError extends boolean = false>(parameters: {
    "If-Match": string;
    routineId: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<ArchiveRoutineResponses, ArchiveRoutineErrors, ThrowOnError>;
export declare const getRoutine: <ThrowOnError extends boolean = false>(parameters: {
    routineId: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<GetRoutineResponses, GetRoutineErrors, ThrowOnError>;
export declare const updateRoutine: <ThrowOnError extends boolean = false>(parameters: {
    "If-Match": string;
    routineId: string;
    routinePatch: RoutinePatch;
}, options?: Options<never, ThrowOnError>) => RequestResult<UpdateRoutineResponses, UpdateRoutineErrors, ThrowOnError>;
export declare const addSession: <ThrowOnError extends boolean = false>(parameters: {
    "If-Match": string;
    routineId: string;
    sessionWrite: SessionWrite;
}, options?: Options<never, ThrowOnError>) => RequestResult<AddSessionResponses, AddSessionErrors, ThrowOnError>;
export declare const deleteSession: <ThrowOnError extends boolean = false>(parameters: {
    "If-Match": string;
    routineId: string;
    sessionId: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<DeleteSessionResponses, DeleteSessionErrors, ThrowOnError>;
export declare const getSession: <ThrowOnError extends boolean = false>(parameters: {
    routineId: string;
    sessionId: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<GetSessionResponses, GetSessionErrors, ThrowOnError>;
export declare const replaceSession: <ThrowOnError extends boolean = false>(parameters: {
    "If-Match": string;
    routineId: string;
    sessionId: string;
    sessionWrite: SessionWrite;
}, options?: Options<never, ThrowOnError>) => RequestResult<ReplaceSessionResponses, ReplaceSessionErrors, ThrowOnError>;
export declare const listSnapshots: <ThrowOnError extends boolean = false>(parameters: {
    routineId: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<ListSnapshotsResponses, ListSnapshotsErrors, ThrowOnError>;
export declare const captureSnapshot: <ThrowOnError extends boolean = false>(parameters: {
    "If-Match": string;
    "Idempotency-Key": string;
    routineId: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<CaptureSnapshotResponses, CaptureSnapshotErrors, ThrowOnError>;
export declare const getSnapshot: <ThrowOnError extends boolean = false>(parameters: {
    routineId: string;
    snapshotId: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<GetSnapshotResponses, GetSnapshotErrors, ThrowOnError>;
/**
 * Reads the session definition and composes matching exercise logs from Exercise Service. The caller's delegated identity must be propagated to Exercise Service.
 *
 */
export declare const listSessionExerciseRecords: <ThrowOnError extends boolean = false>(parameters: {
    routineId: string;
    sessionId: string;
    limit?: number;
    cursor?: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<ListSessionExerciseRecordsResponses, ListSessionExerciseRecordsErrors, ThrowOnError>;
//# sourceMappingURL=sdk.gen.d.ts.map