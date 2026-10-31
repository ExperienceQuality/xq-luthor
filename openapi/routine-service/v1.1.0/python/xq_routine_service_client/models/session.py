from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exercise_prescription import ExercisePrescription


T = TypeVar("T", bound="Session")


@_attrs_define
class Session:
    """
    Attributes:
        id (UUID):
        name (str):
        position (int):
        exercises (list[ExercisePrescription]):
    """

    id: UUID
    name: str
    position: int
    exercises: list[ExercisePrescription]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = str(self.id)

        name = self.name

        position = self.position

        exercises = []
        for exercises_item_data in self.exercises:
            exercises_item = exercises_item_data.to_dict()
            exercises.append(exercises_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "name": name,
                "position": position,
                "exercises": exercises,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_prescription import ExercisePrescription  # noqa: PLC0415

        d = dict(src_dict)
        id = UUID(d.pop("id"))

        name = d.pop("name")

        position = d.pop("position")

        exercises = []
        _exercises = d.pop("exercises")
        for exercises_item_data in _exercises:
            exercises_item = ExercisePrescription.from_dict(exercises_item_data)

            exercises.append(exercises_item)

        session = cls(
            id=id,
            name=name,
            position=position,
            exercises=exercises,
        )

        session.additional_properties = d
        return session

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
