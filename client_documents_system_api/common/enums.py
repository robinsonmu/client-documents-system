from enum import auto
from fastapi_utils.enums import StrEnum


class FilesRequestStatus(StrEnum):
    reviewed = auto()
    not_reviewed = auto()
    returned = auto()
