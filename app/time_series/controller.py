import pandas as pd
from app import csv_controller


def get_time_series(filepath):
    dtype_spec = {
        'id': int,
        'variable': str,
        'organization': str,
        'value': float,
    }
    parse_date_spec = ['timestamp', 'ingestion_time']
    df = csv_controller.read_csv(filepath, dtype_spec, parse_date_spec)
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S%z')
    df['ingestion_time'] = df['ingestion_time'].dt.strftime('%Y-%m-%dT%H:%M:%S%z')
    data = df.to_dict(orient="records")
    print(data)
    return data
