
from typing import List
from fastapi import APIRouter, HTTPException

from app.organizations.controller import get_organizations
# from app.organizations.schemas import  Organizations


router = APIRouter(prefix='/organizations', tags=['users'])


@router.get(path="/", response_model=dict)
def getOrganizations():

    organizations = get_organizations(
        'documents/organization_and_zones_dataset.csv')

    if organizations is None:
        raise HTTPException(status_code=404, detail="Time series not found")
    return organizations
