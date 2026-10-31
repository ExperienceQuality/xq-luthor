from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

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
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        name = self.name

        sets = self.sets

        repetitions = self.repetitions

        weight_kg = self.weight_kg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        exercise_prescription.additional_properties = d
        return exercise_prescription

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
