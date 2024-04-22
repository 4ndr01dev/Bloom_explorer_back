import pandas as pd
from app import csv_controller


def gat_data_set(filepath):
    dtype_spec = {
        'id': int,
        'variable': str,
        'organization': str,
        'value': float,
    }
    parse_date_spec = ['timestamp', 'ingestion_time']
    df = csv_controller.read_csv(filepath, dtype_spec, parse_date_spec)
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S%z')
    df['ingestion_time'] = df['ingestion_time'].dt.strftime(
        '%Y-%m-%dT%H:%M:%S%z')
    return df


def get_time_series(filepath):
    df = gat_data_set(filepath)
    data = df.to_dict(orient="records")
    print(data)
    return data


def get_time_series_grouped_by(filepath):
    df = gat_data_set(filepath)
    dfs = {name: group for name, group in df.groupby('organization')}
    dfs_adasa = {name: group for name,
                 group in dfs['adasa'].groupby('variable')}
    dfs_gsinima = {name: group for name,
                   group in dfs['gsinima'].groupby('variable')}

    adasa = {'values':
             {'CHL-01': dfs_adasa['CHL-01'].to_dict(
                 orient="records"), 'SPM-01': dfs_adasa['SPM-01'].to_dict(orient="records")}
             }
    gsinima = {'values':
               {'CHL-01': dfs_gsinima['CHL-01'].to_dict(
                   orient="records"), 'SPM-01': dfs_gsinima['SPM-01'].to_dict(orient="records")}
               }
    data = {'organizations': {'adasa': adasa, 'gsinima': gsinima}}
    return data


def get_time_series_grouped_by_organization(filepath, organization_name):
    if (organization_name != 'adasa' and organization_name != 'gsinima'):
        return {}
    df = gat_data_set(filepath)
    dfs = {name: group for name, group in df.groupby('organization')}
    dfs_adasa = {name: group for name,
                 group in dfs[organization_name].groupby('variable')}
    organization = {'values':
                    {'CHL-01': dfs_adasa['CHL-01'].to_dict(
                        orient="records"), 'SPM-01': dfs_adasa['SPM-01'].to_dict(orient="records")}
                    }

    data = {organization_name: organization}
    return data
