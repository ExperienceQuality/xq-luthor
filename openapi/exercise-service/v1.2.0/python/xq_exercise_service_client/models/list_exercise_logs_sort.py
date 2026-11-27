from enum import StrEnum


class ListExerciseLogsSort(StrEnum):
    HIGHESTSETVOLUME = "highestSetVolume"
    LOGGEDAT = "loggedAt"

    def __str__(self) -> str:
        return str(self.value)
