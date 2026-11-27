from __future__ import annotations

import datetime
from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define

T = TypeVar("T", bound="ExerciseSummary")


@_attrs_define
class ExerciseSummary:
    """
    Attributes:
        exercise_name (str):
        log_count (int):
        last_logged_at (datetime.datetime):
    """

    exercise_name: str
    log_count: int
    last_logged_at: datetime.datetime

    def to_dict(self) -> dict[str, Any]:
        exercise_name = self.exercise_name

        log_count = self.log_count

        last_logged_at = self.last_logged_at.isoformat()

        field_dict: dict[str, Any] = {}

        field_dict.update(
            {
                "exerciseName": exercise_name,
                "logCount": log_count,
                "lastLoggedAt": last_logged_at,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        exercise_name = d.pop("exerciseName")

        log_count = d.pop("logCount")

        last_logged_at = datetime.datetime.fromisoformat(d.pop("lastLoggedAt"))

        exercise_summary = cls(
            exercise_name=exercise_name,
            log_count=log_count,
            last_logged_at=last_logged_at,
        )

        return exercise_summary
