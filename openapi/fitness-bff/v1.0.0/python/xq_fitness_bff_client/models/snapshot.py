from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.snapshot_entries_item import SnapshotEntriesItem


T = TypeVar("T", bound="Snapshot")


@_attrs_define
class Snapshot:
    """
    Attributes:
        id (UUID):
        captured_at (datetime.datetime):
        entries (list[SnapshotEntriesItem]):
    """

    id: UUID
    captured_at: datetime.datetime
    entries: list[SnapshotEntriesItem]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        captured_at = self.captured_at.isoformat()

        entries = []
        for entries_item_data in self.entries:
            entries_item = entries_item_data.to_dict()
            entries.append(entries_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "capturedAt": captured_at,
                "entries": entries,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.snapshot_entries_item import SnapshotEntriesItem  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        captured_at = datetime.datetime.fromisoformat(d.pop("capturedAt"))

        entries = []
        _entries = d.pop("entries")
        for entries_item_data in _entries:
            entries_item = SnapshotEntriesItem.from_dict(entries_item_data)

            entries.append(entries_item)

        snapshot = cls(
            id=id,
            captured_at=captured_at,
            entries=entries,
        )

        snapshot.additional_properties = d
        return snapshot

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
