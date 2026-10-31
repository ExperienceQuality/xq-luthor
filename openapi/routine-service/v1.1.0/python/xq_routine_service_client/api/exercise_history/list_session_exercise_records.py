from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.exercise_record_page import ExerciseRecordPage
from ...models.problem import Problem
from ...types import UNSET, Response, Unset


def _get_kwargs(
    routine_id: UUID,
    *,
    session_id: UUID,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    json_session_id = str(session_id)
    params["sessionId"] = json_session_id

    params["limit"] = limit

    params["cursor"] = cursor

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/routines/{routine_id}/exercise-records".format(
            routine_id=quote(str(routine_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> ExerciseRecordPage | Problem | None:
    if response.status_code == 200:
        response_200 = ExerciseRecordPage.from_dict(response.json())

        return response_200

    if response.status_code == 400:
        response_400 = Problem.from_dict(response.json())

        return response_400

    if response.status_code == 401:
        response_401 = Problem.from_dict(response.json())

        return response_401

    if response.status_code == 404:
        response_404 = Problem.from_dict(response.json())

        return response_404

    if response.status_code == 502:
        response_502 = Problem.from_dict(response.json())

        return response_502

    if response.status_code == 503:
        response_503 = Problem.from_dict(response.json())

        return response_503

    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: AuthenticatedClient | Client, response: httpx.Response
) -> Response[ExerciseRecordPage | Problem]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    routine_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    session_id: UUID,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> Response[ExerciseRecordPage | Problem]:
    """Reads the session definition and composes matching exercise logs from Exercise Service. The caller's
    delegated identity must be propagated to Exercise Service.

    Args:
        routine_id (UUID):
        session_id (UUID):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExerciseRecordPage | Problem]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        session_id=session_id,
        limit=limit,
        cursor=cursor,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    routine_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    session_id: UUID,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> ExerciseRecordPage | Problem | None:
    """Reads the session definition and composes matching exercise logs from Exercise Service. The caller's
    delegated identity must be propagated to Exercise Service.

    Args:
        routine_id (UUID):
        session_id (UUID):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExerciseRecordPage | Problem
    """

    return sync_detailed(
        routine_id=routine_id,
        client=client,
        session_id=session_id,
        limit=limit,
        cursor=cursor,
    ).parsed


async def asyncio_detailed(
    routine_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    session_id: UUID,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> Response[ExerciseRecordPage | Problem]:
    """Reads the session definition and composes matching exercise logs from Exercise Service. The caller's
    delegated identity must be propagated to Exercise Service.

    Args:
        routine_id (UUID):
        session_id (UUID):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[ExerciseRecordPage | Problem]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        session_id=session_id,
        limit=limit,
        cursor=cursor,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    routine_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    session_id: UUID,
    limit: int | Unset = 20,
    cursor: str | Unset = UNSET,
) -> ExerciseRecordPage | Problem | None:
    """Reads the session definition and composes matching exercise logs from Exercise Service. The caller's
    delegated identity must be propagated to Exercise Service.

    Args:
        routine_id (UUID):
        session_id (UUID):
        limit (int | Unset):  Default: 20.
        cursor (str | Unset):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        ExerciseRecordPage | Problem
    """

    return (
        await asyncio_detailed(
            routine_id=routine_id,
            client=client,
            session_id=session_id,
            limit=limit,
            cursor=cursor,
        )
    ).parsed
