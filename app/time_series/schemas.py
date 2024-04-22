from datetime import datetime
from pydantic import BaseModel


class TimeSeriesItem(BaseModel):
    timestamp: datetime
    variable: str
    organization: str
    value: float | None
    ingestion_time: datetime


class TimeSeriesGroupedItem(BaseModel):
    times_series: dict
