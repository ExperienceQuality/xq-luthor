from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExercisePrescription")


@_attrs_define
class ExercisePrescription:
    """
    Attributes:
        name (str):
        sets (int):
        repetitions (int):
        weight_kg (float):
    """

    name: str
    sets: int
    repetitions: int
    weight_kg: float

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sets = self.sets

        repetitions = self.repetitions

        weight_kg = self.weight_kg

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "name": name,
                "sets": sets,
                "repetitions": repetitions,
                "weightKg": weight_kg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        name = d.pop("name")

        sets = d.pop("sets")

        repetitions = d.pop("repetitions")

        weight_kg = d.pop("weightKg")

        exercise_prescription = cls(
            name=name,
            sets=sets,
            repetitions=repetitions,
            weight_kg=weight_kg,
        )

        return exercise_prescription
