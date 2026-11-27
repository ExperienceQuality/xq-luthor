import { type Client, type ClientMeta, type Options as Options2, type RequestResult, type TDataShape } from './client';
import type { CreateExerciseLogErrors, CreateExerciseLogRequest, CreateExerciseLogResponses, GetExerciseLogErrors, GetExerciseLogResponses, ListDistinctExercisesErrors, ListDistinctExercisesResponses, ListExerciseLogsErrors, ListExerciseLogsResponses } from './types.gen';
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
/**
 * List the authenticated user's exercise logs.
 */
export declare const listExerciseLogs: <ThrowOnError extends boolean = false>(parameters?: {
    exerciseName?: string;
    exerciseNames?: Array<string>;
    sort?: "loggedAt" | "highestSetVolume";
    limit?: number;
    cursor?: string;
}, options?: Options<never, ThrowOnError>) => RequestResult<ListExerciseLogsResponses, ListExerciseLogsErrors, ThrowOnError>;
/**
 * Create an exercise log for the authenticated user.
 */
export declare const createExerciseLog: <ThrowOnError extends boolean = false>(parameters: {
    createExerciseLogRequest: CreateExerciseLogRequest;
}, options?: Options<never, ThrowOnError>) => RequestResult<CreateExerciseLogResponses, CreateExerciseLogErrors, ThrowOnError>;
/**
 * List distinct exercise names used by the authenticated user.
 */
export declare const listDistinctExercises: <ThrowOnError extends boolean = false>(options?: Options<never, ThrowOnError>) => RequestResult<ListDistinctExercisesResponses, ListDistinctExercisesErrors, ThrowOnError>;
/**
 * Get one exercise log owned by the authenticated user.
 */
export declare const getExerciseLog: <ThrowOnError extends boolean = false>(parameters: {
    exerciseLogId: number;
}, options?: Options<never, ThrowOnError>) => RequestResult<GetExerciseLogResponses, GetExerciseLogErrors, ThrowOnError>;
//# sourceMappingURL=sdk.gen.d.ts.map