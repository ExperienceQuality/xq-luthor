from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.snapshot import Snapshot
from ...types import Response


def _get_kwargs(
    routine_id: UUID,
    snapshot_id: UUID,
) -> dict[str, Any]:

    _kwargs: dict[str, Any] = {
        "method": "get",
        "url": "/api/v1/routines/{routine_id}/snapshots/{snapshot_id}".format(
            routine_id=quote(str(routine_id), safe=""),
            snapshot_id=quote(str(snapshot_id), safe=""),
        ),
    }

    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Problem | Snapshot | None:
    if response.status_code == 200:
        response_200 = Snapshot.from_dict(response.json())

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Problem | Snapshot]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    routine_id: UUID,
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Problem | Snapshot]:
    """
    Args:
        routine_id (UUID):
        snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Snapshot]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        snapshot_id=snapshot_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    routine_id: UUID,
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Problem | Snapshot | None:
    """
    Args:
        routine_id (UUID):
        snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Snapshot
    """

    return sync_detailed(
        routine_id=routine_id,
        snapshot_id=snapshot_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    routine_id: UUID,
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Response[Problem | Snapshot]:
    """
    Args:
        routine_id (UUID):
        snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Snapshot]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        snapshot_id=snapshot_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    routine_id: UUID,
    snapshot_id: UUID,
    *,
    client: AuthenticatedClient | Client,
) -> Problem | Snapshot | None:
    """
    Args:
        routine_id (UUID):
        snapshot_id (UUID):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Snapshot
    """

    return (
        await asyncio_detailed(
            routine_id=routine_id,
            snapshot_id=snapshot_id,
            client=client,
        )
    ).parsed
