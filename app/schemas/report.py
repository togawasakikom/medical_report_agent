from pydantic import BaseModel
from typing import Optional

class Indicator(BaseModel):
    name: str
    value: float
    unit: Optional[str] = None
    referance_range: Optional[str] = None
    status: Optional[str]


class Report_Response(BaseModel):
    file_name: str
    message: str
    indicators: list[Indicator]

    