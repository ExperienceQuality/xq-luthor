from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exercise_log_sets_item import ExerciseLogSetsItem


T = TypeVar("T", bound="ExerciseLog")


@_attrs_define
class ExerciseLog:
    """
    Attributes:
        id (int):
        exercise_name (str):
        logged_at (datetime.datetime):
        sets (list[ExerciseLogSetsItem]):
        highest_set_volume_kg (float):
    """

    id: int
    exercise_name: str
    logged_at: datetime.datetime
    sets: list[ExerciseLogSetsItem]
    highest_set_volume_kg: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        exercise_name = self.exercise_name

        logged_at = self.logged_at.isoformat()

        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        highest_set_volume_kg = self.highest_set_volume_kg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "exerciseName": exercise_name,
                "loggedAt": logged_at,
                "sets": sets,
                "highestSetVolumeKg": highest_set_volume_kg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_log_sets_item import ExerciseLogSetsItem  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        exercise_name = d.pop("exerciseName")

        logged_at = datetime.datetime.fromisoformat(d.pop("loggedAt"))

        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = ExerciseLogSetsItem.from_dict(sets_item_data)

            sets.append(sets_item)

        highest_set_volume_kg = d.pop("highestSetVolumeKg")

        exercise_log = cls(
            id=id,
            exercise_name=exercise_name,
            logged_at=logged_at,
            sets=sets,
            highest_set_volume_kg=highest_set_volume_kg,
        )

        exercise_log.additional_properties = d
        return exercise_log

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
