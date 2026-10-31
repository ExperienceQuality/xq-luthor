from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.exercise_set_request import ExerciseSetRequest


T = TypeVar("T", bound="CreateExerciseLogRequest")


@_attrs_define
class CreateExerciseLogRequest:
    """
    Attributes:
        exercise_name (str):
        sets (list[ExerciseSetRequest]):
        logged_at (datetime.datetime | Unset): Optional client-observed workout time. Server uses current time when
            omitted.
    """

    exercise_name: str
    sets: list[ExerciseSetRequest]
    logged_at: datetime.datetime | Unset = UNSET

    def to_dict(self) -> dict[str, Any]:
        exercise_name = self.exercise_name

        sets = []
        for sets_item_data in self.sets:
            sets_item = sets_item_data.to_dict()
            sets.append(sets_item)

        logged_at: str | Unset = UNSET
        if not isinstance(self.logged_at, Unset):
            logged_at = self.logged_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "exerciseName": exercise_name,
                "sets": sets,
            }
        )
        if logged_at is not UNSET:
            field_dict["loggedAt"] = logged_at

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_set_request import ExerciseSetRequest  # noqa: PLC0415

        d = dict(src_dict)
        exercise_name = d.pop("exerciseName")

        sets = []
        _sets = d.pop("sets")
        for sets_item_data in _sets:
            sets_item = ExerciseSetRequest.from_dict(sets_item_data)

            sets.append(sets_item)

        _logged_at = d.pop("loggedAt", UNSET)
        logged_at: datetime.datetime | Unset
        if isinstance(_logged_at, Unset):
            logged_at = UNSET
        else:
            logged_at = datetime.datetime.fromisoformat(_logged_at)

        create_exercise_log_request = cls(
            exercise_name=exercise_name,
            sets=sets,
            logged_at=logged_at,
        )

        return create_exercise_log_request
