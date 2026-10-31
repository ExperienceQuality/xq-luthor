from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExerciseSetRequest")


@_attrs_define
class ExerciseSetRequest:
    """
    Attributes:
        set_number (int):
        weight_kg (float):
        reps (int):
    """

    set_number: int
    weight_kg: float
    reps: int

    def to_dict(self) -> dict[str, Any]:
        set_number = self.set_number

        weight_kg = self.weight_kg

        reps = self.reps

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "setNumber": set_number,
                "weightKg": weight_kg,
                "reps": reps,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        set_number = d.pop("setNumber")

        weight_kg = d.pop("weightKg")

        reps = d.pop("reps")

        exercise_set_request = cls(
            set_number=set_number,
            weight_kg=weight_kg,
            reps=reps,
        )

        return exercise_set_request
