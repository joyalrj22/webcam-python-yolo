from enum import Enum

from pydantic import BaseModel


class FilterType(Enum):
    NONE = 0
    OBJECT_DETECTION = 1
    BOX_FILTER = 2
    GAUSSIAN_FILTER = 3
    MEDIAN_FILTER = 4
    BILATERAL_FILTER = 5


class Filter(BaseModel):
    type: FilterType
