from http import HTTPStatus
from typing import Any
from urllib.parse import quote

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exercise_log import ExerciseLog
from ...models.problem import Problem
from ...types import Response


def _get_kwargs(
    exercise_log_id: int,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/exercise-logs/{exercise_log_id}".format(
            exercise_log_id=quote(str(exercise_log_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> ExerciseLog | Problem | None:
    if response.status_code == 200:
        response_200 = ExerciseLog.from_dict(response.json())

        return response_200

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExerciseLog | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    exercise_log_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExerciseLog | Problem]:
    """Get one exercise log owned by the authenticated user.

    Args:
        exercise_log_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExerciseLog | Problem]
    """

    kwargs = _get_kwargs(
        exercise_log_id=exercise_log_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    exercise_log_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ExerciseLog | Problem | None:
    """Get one exercise log owned by the authenticated user.

    Args:
        exercise_log_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExerciseLog | Problem
    """

    return sync_detailed(
        exercise_log_id=exercise_log_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    exercise_log_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> Response[ExerciseLog | Problem]:
    """Get one exercise log owned by the authenticated user.

    Args:
        exercise_log_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExerciseLog | Problem]
    """

    kwargs = _get_kwargs(
        exercise_log_id=exercise_log_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    exercise_log_id: int,
    *,
    client: AuthenticatedClient | Client,
) -> ExerciseLog | Problem | None:
    """Get one exercise log owned by the authenticated user.

    Args:
        exercise_log_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExerciseLog | Problem
    """

    return (
        await asyncio_detailed(
            exercise_log_id=exercise_log_id,
            client=client,
        )
    ).parsed
