from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define

if TYPE_CHECKING:
    from ..models.exercise_reference import ExerciseReference


T = TypeVar("T", bound="SessionRequest")


@_attrs_define
class SessionRequest:
    """
    Attributes:
        name (str):
        position (int):
        exercises (list[ExerciseReference]):
    """

    name: str
    position: int
    exercises: list[ExerciseReference]

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        position = self.position

        exercises = []
        for exercises_item_data in self.exercises:
            exercises_item = exercises_item_data.to_dict()
            exercises.append(exercises_item)

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "position": position,
                "exercises": exercises,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_reference import ExerciseReference  # noqa: PLC0415

        d = dict(src_dict)
        name = d.pop("name")

        position = d.pop("position")

        exercises = []
        _exercises = d.pop("exercises")
        for exercises_item_data in _exercises:
            exercises_item = ExerciseReference.from_dict(exercises_item_data)

            exercises.append(exercises_item)

        session_request = cls(
            name=name,
            position=position,
            exercises=exercises,
        )

        return session_request
