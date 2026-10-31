from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exercise_log_page import ExerciseLogPage
from ...models.list_exercise_logs_sort import ListExerciseLogsSort
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    exercise_name: str | Unset = UNSET,
    exercise_names: list[str] | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["exerciseName"] = exercise_name

    json_exercise_names: list[str] | Unset = UNSET
    if not isinstance(exercise_names, Unset):
        json_exercise_names = exercise_names

    params["exerciseNames"] = json_exercise_names

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/exercise-logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExerciseLogPage | Problem | None:
    if response.status_code == 200:
        response_200 = ExerciseLogPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExerciseLogPage | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient | Client,
    exercise_name: str | Unset = UNSET,
    exercise_names: list[str] | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> Response[ExerciseLogPage | Problem]:
    """List the authenticated user's exercise logs.

    Args:
        exercise_name (str | Unset):
        exercise_names (list[str] | Unset):
        sort (ListExerciseLogsSort | Unset):  Default: ListExerciseLogsSort.LOGGEDAT.
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExerciseLogPage | Problem]
    """

    kwargs = _get_kwargs(
        exercise_name=exercise_name,
        exercise_names=exercise_names,
        sort=sort,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    exercise_name: str | Unset = UNSET,
    exercise_names: list[str] | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> ExerciseLogPage | Problem | None:
    """List the authenticated user's exercise logs.

    Args:
        exercise_name (str | Unset):
        exercise_names (list[str] | Unset):
        sort (ListExerciseLogsSort | Unset):  Default: ListExerciseLogsSort.LOGGEDAT.
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExerciseLogPage | Problem
    """

    return sync_detailed(
        client=client,
        exercise_name=exercise_name,
        exercise_names=exercise_names,
        sort=sort,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    exercise_name: str | Unset = UNSET,
    exercise_names: list[str] | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> Response[ExerciseLogPage | Problem]:
    """List the authenticated user's exercise logs.

    Args:
        exercise_name (str | Unset):
        exercise_names (list[str] | Unset):
        sort (ListExerciseLogsSort | Unset):  Default: ListExerciseLogsSort.LOGGEDAT.
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExerciseLogPage | Problem]
    """

    kwargs = _get_kwargs(
        exercise_name=exercise_name,
        exercise_names=exercise_names,
        sort=sort,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    exercise_name: str | Unset = UNSET,
    exercise_names: list[str] | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> ExerciseLogPage | Problem | None:
    """List the authenticated user's exercise logs.

    Args:
        exercise_name (str | Unset):
        exercise_names (list[str] | Unset):
        sort (ListExerciseLogsSort | Unset):  Default: ListExerciseLogsSort.LOGGEDAT.
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExerciseLogPage | Problem
    """

    return (
        await asyncio_detailed(
            client=client,
            exercise_name=exercise_name,
            exercise_names=exercise_names,
            sort=sort,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
