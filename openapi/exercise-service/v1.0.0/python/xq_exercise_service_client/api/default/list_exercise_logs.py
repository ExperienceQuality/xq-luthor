from http import HTTPStatus
from typing import Any

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exercise_log import ExerciseLog
from ...models.list_exercise_logs_sort import ListExerciseLogsSort
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    exercise_name: str | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["exerciseName"] = exercise_name

    json_sort: str | Unset = UNSET
    if not isinstance(sort, Unset):
        json_sort = sort.value

    params["sort"] = json_sort

    params["limit"] = limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/exercise-logs",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Problem | list[ExerciseLog] | None:
    if response.status_code == 200:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = ExerciseLog.from_dict(response_200_item_data)

            response_200.append(response_200_item)

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[Problem | list[ExerciseLog]]:
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
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
) -> Response[Problem | list[ExerciseLog]]:
    """List exercise logs

    Args:
        exercise_name (str | Unset):
        sort (ListExerciseLogsSort | Unset):  Default: ListExerciseLogsSort.LOGGEDAT.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | list[ExerciseLog]]
    """

    kwargs = _get_kwargs(
        exercise_name=exercise_name,
        sort=sort,
        limit=limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient | Client,
    exercise_name: str | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
) -> Problem | list[ExerciseLog] | None:
    """List exercise logs

    Args:
        exercise_name (str | Unset):
        sort (ListExerciseLogsSort | Unset):  Default: ListExerciseLogsSort.LOGGEDAT.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | list[ExerciseLog]
    """

    return sync_detailed(
        client=client,
        exercise_name=exercise_name,
        sort=sort,
        limit=limit,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient | Client,
    exercise_name: str | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
) -> Response[Problem | list[ExerciseLog]]:
    """List exercise logs

    Args:
        exercise_name (str | Unset):
        sort (ListExerciseLogsSort | Unset):  Default: ListExerciseLogsSort.LOGGEDAT.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | list[ExerciseLog]]
    """

    kwargs = _get_kwargs(
        exercise_name=exercise_name,
        sort=sort,
        limit=limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient | Client,
    exercise_name: str | Unset = UNSET,
    sort: ListExerciseLogsSort | Unset = ListExerciseLogsSort.LOGGEDAT,
    limit: int | Unset = 20,
) -> Problem | list[ExerciseLog] | None:
    """List exercise logs

    Args:
        exercise_name (str | Unset):
        sort (ListExerciseLogsSort | Unset):  Default: ListExerciseLogsSort.LOGGEDAT.
        limit (int | Unset):  Default: 20.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | list[ExerciseLog]
    """

    return (
        await asyncio_detailed(
            client=client,
            exercise_name=exercise_name,
            sort=sort,
            limit=limit,
        )
    ).parsed
