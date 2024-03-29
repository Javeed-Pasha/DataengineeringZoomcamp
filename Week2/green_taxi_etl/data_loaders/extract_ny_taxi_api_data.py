import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    baseurl = 'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-'

    files = ['10.csv.gz','11.csv.gz','12.csv.gz']
    df =[]

    taxi_dtypes = {
                        'VendorID': pd.Int64Dtype(),
                       # 'lpep_pickup_datetime': pd.Timestamp(),
                        #'lpep_dropoff_datetime': pd.Timestamp(),
                        'store_and_fwd_flag': str,
                        'RatecodeID':  pd.Int64Dtype(),
                        'PULocationID':  pd.Int64Dtype(),
                        'DOLocationID':  pd.Int64Dtype(),
                        'passenger_count':  pd.Int64Dtype(),
                        'trip_distance': float,
                        'fare_amount': float,
                        'extra': float,
                        'mta_tax': float,
                        'tip_amount': float,
                        'tolls_amount': float,
                        'ehail_fee': float,
                        'improvement_surcharge': float,
                        'total_amount': float,
                        'payment_type':  pd.Int64Dtype(),
                        'trip_type':  pd.Int64Dtype(),
                        'congestion_surcharge': float
                    }

    # native date parsing 
    parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    for f in files:
        url =f'{baseurl}{f}'

        df_ = pd.read_csv(
            url, sep=',', compression='gzip', dtype=taxi_dtypes , parse_dates=parse_dates
            )
        
        df.append(df_)

    dfs = pd.concat(df, ignore_index=True)

    return dfs


