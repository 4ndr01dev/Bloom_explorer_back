from app import csv_controller


def get_data_set(filepath):
    dtype_spec = {
        'organization': str,
        'zone_id': int,
        'zone': str,
        'polygon_decoded': str,
    }
    df = csv_controller.read_csv(filepath, dtype_spec)
    return df


def get_organizations(filepath):
    organizations_df = get_data_set(filepath)
    return {'organizations': organizations_df.to_dict(orient="records")}
