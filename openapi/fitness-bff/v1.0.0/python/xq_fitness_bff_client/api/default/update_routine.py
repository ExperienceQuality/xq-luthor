from http import HTTPStatus
from typing import Any
from urllib.parse import quote
from uuid import UUID

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.problem import Problem
from ...models.routine import Routine
from ...models.routine_patch import RoutinePatch
from ...types import Response


def _get_kwargs(
    routine_id: UUID,
    *,
    body: RoutinePatch,
    if_match: str,
) -> dict[str, Any]:
    headers: dict[str, Any] = {}
    headers["If-Match"] = if_match

    _kwargs: dict[str, Any] = {
        "method": "patch",
        "url": "/api/v1/routines/{routine_id}".format(
            routine_id=quote(str(routine_id), safe=""),
        ),
    }

    _kwargs["json"] = body.to_dict()

    headers["Content-Type"] = "application/merge-patch+json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Problem | Routine | None:
    if response.status_code == 200:
        response_200 = Routine.from_dict(response.json())

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

    if response.status_code == 412:
        response_412 = Problem.from_dict(response.json())

        return response_412

    if response.status_code == 428:
        response_428 = Problem.from_dict(response.json())

        return response_428

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


def _build_response(*, client: AuthenticatedClient | Client, response: httpx.Response) -> Response[Problem | Routine]:
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
    body: RoutinePatch,
    if_match: str,
) -> Response[Problem | Routine]:
    """
    Args:
        routine_id (UUID):
        if_match (str):
        body (RoutinePatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Routine]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        body=body,
        if_match=if_match,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    routine_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RoutinePatch,
    if_match: str,
) -> Problem | Routine | None:
    """
    Args:
        routine_id (UUID):
        if_match (str):
        body (RoutinePatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Routine
    """

    return sync_detailed(
        routine_id=routine_id,
        client=client,
        body=body,
        if_match=if_match,
    ).parsed


async def asyncio_detailed(
    routine_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RoutinePatch,
    if_match: str,
) -> Response[Problem | Routine]:
    """
    Args:
        routine_id (UUID):
        if_match (str):
        body (RoutinePatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Problem | Routine]
    """

    kwargs = _get_kwargs(
        routine_id=routine_id,
        body=body,
        if_match=if_match,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    routine_id: UUID,
    *,
    client: AuthenticatedClient | Client,
    body: RoutinePatch,
    if_match: str,
) -> Problem | Routine | None:
    """
    Args:
        routine_id (UUID):
        if_match (str):
        body (RoutinePatch):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Problem | Routine
    """

    return (
        await asyncio_detailed(
            routine_id=routine_id,
            client=client,
            body=body,
            if_match=if_match,
        )
    ).parsed
