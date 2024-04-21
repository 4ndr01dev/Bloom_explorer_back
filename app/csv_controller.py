
from fastapi import HTTPException
import numpy as np
import pandas as pd


def read_csv(filepath: str, dtype_spec: dict = None, parse_dates_spec: list = []):
    try:
        df = pd.read_csv(filepath, dtype=dtype_spec,
                         parse_dates=parse_dates_spec)


        df = df.replace({
            np.inf: 'Inf',
            -np.inf: '-Inf',
            np.nan: None
        })
        
        return df
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
