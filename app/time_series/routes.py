from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.time_series.controller import get_time_series
from app.time_series.schemas import TimeSeriesItem

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

@router.get(path="/grouped_by_variable_organization", response_model=List[TimeSeriesItem])
# TODO agregar filtro (ejemplo : para tipo de organización)
def getAllSeries():

    all_series = get_time_series(
        'documents/timeseries_dataset.csv')

    if all_series is None:
        raise HTTPException(status_code=404, detail="Time series not found")
    return all_series


