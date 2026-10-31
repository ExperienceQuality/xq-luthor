from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExerciseSet")


@_attrs_define
class ExerciseSet:
    """
    Attributes:
        id (int):
        set_number (int):
        weight_kg (float):
        reps (int):
        volume_kg (float): Calculated as weightKg multiplied by reps.
    """

    id: int
    set_number: int
    weight_kg: float
    reps: int
    volume_kg: float

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        set_number = self.set_number

        weight_kg = self.weight_kg

        reps = self.reps

        volume_kg = self.volume_kg

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "id": id,
                "setNumber": set_number,
                "weightKg": weight_kg,
                "reps": reps,
                "volumeKg": volume_kg,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        id = d.pop("id")

        set_number = d.pop("setNumber")

        weight_kg = d.pop("weightKg")

        reps = d.pop("reps")

        volume_kg = d.pop("volumeKg")

        exercise_set = cls(
            id=id,
            set_number=set_number,
            weight_kg=weight_kg,
            reps=reps,
            volume_kg=volume_kg,
        )

        return exercise_set
