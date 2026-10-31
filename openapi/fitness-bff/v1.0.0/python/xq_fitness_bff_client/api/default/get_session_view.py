from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.session_view import SessionView
from ...types import UNSET, Response, Unset


def _get_kwargs(
    routine_id: UUID,
    session_id: UUID,
    *,
    history_limit: int | Unset = 5,
) -> dict[str, Any]:

    params: dict[str, Any] = {}

    params["historyLimit"] = history_limit

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/routines/{routine_id}/sessions/{session_id}/view".format(
            routine_id=quote(str(routine_id), safe=""),
            session_id=quote(str(session_id), safe=""),
        ),
        "params": params,
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Problem | SessionView | None:
    if response.status_code == 200:
        response_200 = SessionView.from_dict(response.json())

        return response_200

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
) -> Response[Problem | SessionView]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    routine_id: UUID,
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    history_limit: int | Unset = 5,
) -> Response[Problem | SessionView]:
    """Compose a session prescription and recent exercise history.

    Args:
        routine_id (UUID):
        session_id (UUID):
        history_limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SessionView]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        session_id=session_id,
        history_limit=history_limit,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    routine_id: UUID,
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    history_limit: int | Unset = 5,
) -> Problem | SessionView | None:
    """Compose a session prescription and recent exercise history.

    Args:
        routine_id (UUID):
        session_id (UUID):
        history_limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SessionView
    """

    return sync_detailed(
        routine_id=routine_id,
        session_id=session_id,
        client=client,
        history_limit=history_limit,
    ).parsed


async def asyncio_detailed(
    routine_id: UUID,
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    history_limit: int | Unset = 5,
) -> Response[Problem | SessionView]:
    """Compose a session prescription and recent exercise history.

    Args:
        routine_id (UUID):
        session_id (UUID):
        history_limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | SessionView]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        session_id=session_id,
        history_limit=history_limit,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    routine_id: UUID,
    session_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    history_limit: int | Unset = 5,
) -> Problem | SessionView | None:
    """Compose a session prescription and recent exercise history.

    Args:
        routine_id (UUID):
        session_id (UUID):
        history_limit (int | Unset):  Default: 5.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | SessionView
    """

    return (
        await asyncio_detailed(
            routine_id=routine_id,
            session_id=session_id,
            client=client,
            history_limit=history_limit,
        )
    ).parsed
