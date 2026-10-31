from enum import StrEnum


class SnapshotEntriesItemRepetitionsProgress(StrEnum):
    DECREASED = "decreased"
    FIRST = "first"
    INCREASED = "increased"
    SAME = "same"

    def __str__(self) -> str:
        return str(self.value)
