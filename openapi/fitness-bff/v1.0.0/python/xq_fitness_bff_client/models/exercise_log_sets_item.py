from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="ExerciseLogSetsItem")


@_attrs_define
class ExerciseLogSetsItem:
    """
    Attributes:
        id (int):
        set_number (int):
        weight_kg (float):
        reps (int):
        volume_kg (float):
    """

    id: int
    set_number: int
    weight_kg: float
    reps: int
    volume_kg: float
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        id = self.id

        set_number = self.set_number

        weight_kg = self.weight_kg

        reps = self.reps

        volume_kg = self.volume_kg

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        exercise_log_sets_item = cls(
            id=id,
            set_number=set_number,
            weight_kg=weight_kg,
            reps=reps,
            volume_kg=volume_kg,
        )

        exercise_log_sets_item.additional_properties = d
        return exercise_log_sets_item

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
