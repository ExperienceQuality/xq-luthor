from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

T = TypeVar("T", bound="CreateExerciseLogRequestSetsItem")


@_attrs_define
class CreateExerciseLogRequestSetsItem:
    """
    Attributes:
        set_number (int):
        weight_kg (float):
        reps (int):
    """

    set_number: int
    weight_kg: float
    reps: int
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        set_number = self.set_number

        weight_kg = self.weight_kg

        reps = self.reps

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
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

        create_exercise_log_request_sets_item = cls(
            set_number=set_number,
            weight_kg=weight_kg,
            reps=reps,
        )

        create_exercise_log_request_sets_item.additional_properties = d
        return create_exercise_log_request_sets_item

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
