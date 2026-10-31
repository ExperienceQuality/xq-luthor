from enum import StrEnum


class SnapshotEntriesItemWeightProgress(StrEnum):
    DECREASED = "decreased"
    FIRST = "first"
    INCREASED = "increased"
    SAME = "same"

    def __str__(self) -> str:
        return str(self.value)
