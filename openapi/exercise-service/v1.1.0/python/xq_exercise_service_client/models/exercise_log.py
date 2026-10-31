from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.exercise_set import ExerciseSet


T = TypeVar("T", bound="ExerciseLog")


@_attrs_define
class ExerciseLog:
    """
    Attributes:
        id (int):
        exercise_name (str):
        logged_at (datetime.datetime):
        sets (list[ExerciseSet]):
        highest_set_volume_kg (float): Maximum weightKg multiplied by reps among the log's sets.
    """

    id: int
    exercise_name: str
    logged_at: datetime.datetime
    sets: list[ExerciseSet]
    highest_set_volume_kg: float

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
        from ..models.exercise_set import ExerciseSet  # noqa: PLC0415

        d = dict(src_dict)
        id = d.pop("id")

        exercise_name = d.pop("exerciseName")

        logged_at = datetime.datetime.fromisoformat(d.pop("loggedAt"))

        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = ExerciseSet.from_dict(sets_item_data)

            sets.append(sets_item)

        highest_set_volume_kg = d.pop("highestSetVolumeKg")

        exercise_log = cls(
            id=id,
            exercise_name=exercise_name,
            logged_at=logged_at,
            sets=sets,
            highest_set_volume_kg=highest_set_volume_kg,
        )

        return exercise_log
