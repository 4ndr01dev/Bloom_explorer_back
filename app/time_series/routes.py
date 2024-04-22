from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.time_series.controller import get_time_series, get_time_series_grouped_by, get_time_series_grouped_by_organization
from app.time_series.schemas import TimeSeriesGroupedItem, TimeSeriesItem

router = APIRouter(prefix='/time_series', tags=['users'])


@router.get(path="/", response_model=List[TimeSeriesItem])
def getAllSeries():

    all_series = get_time_series(
        'documents/timeseries_dataset.csv')

    if all_series is None:
        raise HTTPException(status_code=404, detail="Time series not found")
    return all_series

@router.get(path="/grouped_by_variable", response_model=List[TimeSeriesItem])
def getAllSeries():

    all_series = get_time_series(
        'documents/timeseries_dataset.csv')

    if all_series is None:
        raise HTTPException(status_code=404, detail="Time series not found")
    return all_series


@router.get(path="/grouped_by_variable_organization", response_model=dict)
def get_series_full_grouped():
    all_series = get_time_series_grouped_by(
        'documents/timeseries_dataset.csv')

    if all_series is None:
        raise HTTPException(status_code=404, detail="Time series not found")
    return all_series

@router.get(path="/grouped_by_organization", response_model=dict)
def get_series_grouped_by_organization(organization_name):
    all_series = get_time_series_grouped_by_organization(
        'documents/timeseries_dataset.csv',organization_name)

    if all_series is None:
        raise HTTPException(status_code=404, detail="Time series not found")
    return all_series


