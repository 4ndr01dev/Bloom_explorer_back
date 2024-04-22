from pydantic import BaseModel


class Organization(BaseModel):
    id : int
    organization: str
    zone : str
    zone_id : int
    polygon_decoded : str


class Organizations(BaseModel):
    organizations: dict
