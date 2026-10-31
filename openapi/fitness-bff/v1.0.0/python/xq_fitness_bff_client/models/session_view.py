from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar
from uuid import UUID

from attrs import define as _attrs_define
from attrs import field as _attrs_field

if TYPE_CHECKING:
    from ..models.exercise_history_by_name import ExerciseHistoryByName
    from ..models.session import Session


T = TypeVar("T", bound="SessionView")


@_attrs_define
class SessionView:
    """
    Attributes:
        routine_id (UUID):
        session (Session):
        exercise_history (list[ExerciseHistoryByName]):
    """

    routine_id: UUID
    session: Session
    exercise_history: list[ExerciseHistoryByName]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        routine_id = str(self.routine_id)

        session = self.session.to_dict()

        exercise_history = []
        for exercise_history_item_data in self.exercise_history:
            exercise_history_item = exercise_history_item_data.to_dict()
            exercise_history.append(exercise_history_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "routineId": routine_id,
                "session": session,
                "exerciseHistory": exercise_history,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.exercise_history_by_name import ExerciseHistoryByName  # noqa: PLC0415
        from ..models.session import Session  # noqa: PLC0415

        d = dict(src_dict)
        routine_id = UUID(d.pop("routineId"))

        session = Session.from_dict(d.pop("session"))

        exercise_history = []
        _exercise_history = d.pop("exerciseHistory")
        for exercise_history_item_data in _exercise_history:
            exercise_history_item = ExerciseHistoryByName.from_dict(exercise_history_item_data)

            exercise_history.append(exercise_history_item)

        session_view = cls(
            routine_id=routine_id,
            session=session,
            exercise_history=exercise_history,
        )

        session_view.additional_properties = d
        return session_view

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
