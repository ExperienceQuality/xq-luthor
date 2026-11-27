export type ClientOptions = {
    baseUrl: `${string}://${string}` | (string & {});
};
export type RoutineCreate = {
    name: string;
    notes?: string | null;
};
export type RoutinePatch = {
    name?: string;
    notes?: string | null;
};
export type Routine = {
    id: string;
    name: string;
    notes?: string | null;
    archivedAt?: string | null;
    version: number;
    createdAt: string;
    updatedAt: string;
    sessions: Array<Session>;
};
export type RoutineListItem = {
    id: string;
    name: string;
    notes?: string | null;
    archivedAt?: string | null;
    version: number;
    createdAt: string;
    updatedAt: string;
};
export type RoutinePage = {
    items: Array<RoutineListItem>;
    nextCursor: string | null;
};
export type SessionWrite = {
    name: string;
    position: number;
    exercises: Array<ExercisePrescription>;
};
export type Session = {
    id: string;
    name: string;
    position: number;
    exercises: Array<ExercisePrescription>;
};
export type ExercisePrescription = {
    name: string;
    sets: number;
    repetitions: number;
    weightKg: number;
};
export type Snapshot = {
    id: string;
    capturedAt: string;
    entries: Array<SnapshotEntry>;
};
export type SnapshotEntry = {
    name: string;
    sets: number;
    repetitions: number;
    weightKg: number;
    repetitionsProgress: Progress;
    weightProgress: Progress;
};
export type Progress = 'first' | 'increased' | 'decreased' | 'same';
export type ExerciseRecordPage = {
    items: Array<ExerciseRecord>;
    nextCursor: string | null;
};
export type ExerciseRecord = {
    id: number;
    exerciseName: string;
    loggedAt: string;
    sets: Array<{
        id: number;
        setNumber: number;
        weightKg: number;
        reps: number;
        volumeKg: number;
    }>;
    highestSetVolumeKg: number;
};
export type Problem = {
    type: string;
    title: string;
    status: number;
    detail: string;
    code: string;
    violations?: Array<{
        field: string;
        message: string;
    }>;
};
export type RoutineId = string;
export type SessionId = string;
export type Limit = number;
export type Cursor = string;
export type IfMatch = string;
export type LivenessData = {
    body?: never;
    path?: never;
    query?: never;
    url: '/livez';
};
export type LivenessResponses = {
    /**
     * Service is alive.
     */
    200: unknown;
};
export type ReadinessData = {
    body?: never;
    path?: never;
    query?: never;
    url: '/readyz';
};
export type ReadinessResponses = {
    /**
     * Service is ready.
     */
    200: unknown;
};
export type ListRoutinesData = {
    body?: never;
    path?: never;
    query?: {
        limit?: number;
        cursor?: string;
        includeArchived?: boolean;
    };
    url: '/api/v1/routines';
};
export type ListRoutinesErrors = {
    /**
     * Request validation failed.
     */
    400: Problem;
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
};
export type ListRoutinesError = ListRoutinesErrors[keyof ListRoutinesErrors];
export type ListRoutinesResponses = {
    /**
     * Page of routines owned by the authenticated principal.
     */
    200: RoutinePage;
};
export type ListRoutinesResponse = ListRoutinesResponses[keyof ListRoutinesResponses];
export type CreateRoutineData = {
    body: RoutineCreate;
    path?: never;
    query?: never;
    url: '/api/v1/routines';
};
export type CreateRoutineErrors = {
    /**
     * Request validation failed.
     */
    400: Problem;
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
};
export type CreateRoutineError = CreateRoutineErrors[keyof CreateRoutineErrors];
export type CreateRoutineResponses = {
    /**
     * Routine created.
     */
    201: Routine;
};
export type CreateRoutineResponse = CreateRoutineResponses[keyof CreateRoutineResponses];
export type ArchiveRoutineData = {
    body?: never;
    headers: {
        'If-Match': string;
    };
    path: {
        routineId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}';
};
export type ArchiveRoutineErrors = {
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
    /**
     * If-Match does not match the current routine version.
     */
    412: Problem;
    /**
     * Required If-Match header is missing.
     */
    428: Problem;
};
export type ArchiveRoutineError = ArchiveRoutineErrors[keyof ArchiveRoutineErrors];
export type ArchiveRoutineResponses = {
    /**
     * Routine archived; children are retained.
     */
    204: void;
};
export type ArchiveRoutineResponse = ArchiveRoutineResponses[keyof ArchiveRoutineResponses];
export type GetRoutineData = {
    body?: never;
    path: {
        routineId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}';
};
export type GetRoutineErrors = {
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
};
export type GetRoutineError = GetRoutineErrors[keyof GetRoutineErrors];
export type GetRoutineResponses = {
    /**
     * Routine details.
     */
    200: Routine;
};
export type GetRoutineResponse = GetRoutineResponses[keyof GetRoutineResponses];
export type UpdateRoutineData = {
    body: RoutinePatch;
    headers: {
        'If-Match': string;
    };
    path: {
        routineId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}';
};
export type UpdateRoutineErrors = {
    /**
     * Request validation failed.
     */
    400: Problem;
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
    /**
     * If-Match does not match the current routine version.
     */
    412: Problem;
    /**
     * Required If-Match header is missing.
     */
    428: Problem;
};
export type UpdateRoutineError = UpdateRoutineErrors[keyof UpdateRoutineErrors];
export type UpdateRoutineResponses = {
    /**
     * Routine updated.
     */
    200: Routine;
};
export type UpdateRoutineResponse = UpdateRoutineResponses[keyof UpdateRoutineResponses];
export type AddSessionData = {
    body: SessionWrite;
    headers: {
        'If-Match': string;
    };
    path: {
        routineId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}/sessions';
};
export type AddSessionErrors = {
    /**
     * Request validation failed.
     */
    400: Problem;
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
    /**
     * Domain conflict, such as an archived routine.
     */
    409: Problem;
    /**
     * If-Match does not match the current routine version.
     */
    412: Problem;
    /**
     * Required If-Match header is missing.
     */
    428: Problem;
};
export type AddSessionError = AddSessionErrors[keyof AddSessionErrors];
export type AddSessionResponses = {
    /**
     * Session created.
     */
    201: Session;
};
export type AddSessionResponse = AddSessionResponses[keyof AddSessionResponses];
export type DeleteSessionData = {
    body?: never;
    headers: {
        'If-Match': string;
    };
    path: {
        routineId: string;
        sessionId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}/sessions/{sessionId}';
};
export type DeleteSessionErrors = {
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
    /**
     * If-Match does not match the current routine version.
     */
    412: Problem;
    /**
     * Required If-Match header is missing.
     */
    428: Problem;
};
export type DeleteSessionError = DeleteSessionErrors[keyof DeleteSessionErrors];
export type DeleteSessionResponses = {
    /**
     * Session deleted and remaining positions compacted.
     */
    204: void;
};
export type DeleteSessionResponse = DeleteSessionResponses[keyof DeleteSessionResponses];
export type GetSessionData = {
    body?: never;
    path: {
        routineId: string;
        sessionId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}/sessions/{sessionId}';
};
export type GetSessionErrors = {
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
};
export type GetSessionError = GetSessionErrors[keyof GetSessionErrors];
export type GetSessionResponses = {
    /**
     * Session details.
     */
    200: Session;
};
export type GetSessionResponse = GetSessionResponses[keyof GetSessionResponses];
export type ReplaceSessionData = {
    body: SessionWrite;
    headers: {
        'If-Match': string;
    };
    path: {
        routineId: string;
        sessionId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}/sessions/{sessionId}';
};
export type ReplaceSessionErrors = {
    /**
     * Request validation failed.
     */
    400: Problem;
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
    /**
     * Domain conflict, such as an archived routine.
     */
    409: Problem;
    /**
     * If-Match does not match the current routine version.
     */
    412: Problem;
    /**
     * Required If-Match header is missing.
     */
    428: Problem;
};
export type ReplaceSessionError = ReplaceSessionErrors[keyof ReplaceSessionErrors];
export type ReplaceSessionResponses = {
    /**
     * Session replaced.
     */
    200: Session;
};
export type ReplaceSessionResponse = ReplaceSessionResponses[keyof ReplaceSessionResponses];
export type ListSnapshotsData = {
    body?: never;
    path: {
        routineId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}/snapshots';
};
export type ListSnapshotsErrors = {
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
};
export type ListSnapshotsError = ListSnapshotsErrors[keyof ListSnapshotsErrors];
export type ListSnapshotsResponses = {
    /**
     * Up to the two most recent snapshots, newest first.
     */
    200: Array<Snapshot>;
};
export type ListSnapshotsResponse = ListSnapshotsResponses[keyof ListSnapshotsResponses];
export type CaptureSnapshotData = {
    body?: never;
    headers: {
        'If-Match': string;
        'Idempotency-Key': string;
    };
    path: {
        routineId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}/snapshots';
};
export type CaptureSnapshotErrors = {
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
    /**
     * Domain conflict, such as an archived routine.
     */
    409: Problem;
    /**
     * If-Match does not match the current routine version.
     */
    412: Problem;
    /**
     * Required If-Match header is missing.
     */
    428: Problem;
};
export type CaptureSnapshotError = CaptureSnapshotErrors[keyof CaptureSnapshotErrors];
export type CaptureSnapshotResponses = {
    /**
     * Snapshot captured; older snapshots beyond retention are pruned atomically.
     */
    201: Snapshot;
};
export type CaptureSnapshotResponse = CaptureSnapshotResponses[keyof CaptureSnapshotResponses];
export type GetSnapshotData = {
    body?: never;
    path: {
        routineId: string;
        snapshotId: string;
    };
    query?: never;
    url: '/api/v1/routines/{routineId}/snapshots/{snapshotId}';
};
export type GetSnapshotErrors = {
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
};
export type GetSnapshotError = GetSnapshotErrors[keyof GetSnapshotErrors];
export type GetSnapshotResponses = {
    /**
     * Snapshot details.
     */
    200: Snapshot;
};
export type GetSnapshotResponse = GetSnapshotResponses[keyof GetSnapshotResponses];
export type ListSessionExerciseRecordsData = {
    body?: never;
    path: {
        routineId: string;
    };
    query: {
        sessionId: string;
        limit?: number;
        cursor?: string;
    };
    url: '/api/v1/routines/{routineId}/exercise-records';
};
export type ListSessionExerciseRecordsErrors = {
    /**
     * Request validation failed.
     */
    400: Problem;
    /**
     * Missing, invalid, expired, or unacceptable access token.
     */
    401: Problem;
    /**
     * Resource does not exist or is not owned by the authenticated principal.
     */
    404: Problem;
    /**
     * Downstream response was invalid.
     */
    502: Problem;
    /**
     * Exercise Service unavailable; Retry-After may be present.
     */
    503: Problem;
};
export type ListSessionExerciseRecordsError = ListSessionExerciseRecordsErrors[keyof ListSessionExerciseRecordsErrors];
export type ListSessionExerciseRecordsResponses = {
    /**
     * Exercise records matching the session's exercise references.
     */
    200: ExerciseRecordPage;
};
export type ListSessionExerciseRecordsResponse = ListSessionExerciseRecordsResponses[keyof ListSessionExerciseRecordsResponses];
//# sourceMappingURL=types.gen.d.ts.map