import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):

    baseurl = 'https://d37ci6vzurychx.cloudfront.net/trip-data/green_tripdata_2022-'

    files = ['01.parquet','02.parquet','03.parquet','04.parquet','05.parquet','06.parquet','07.parquet','08.parquet','09.parquet','10.parquet','11.parquet','12.parquet']
   #files = ['01.parquet']
    df =[]

    taxi_dtypes = {
                        'VendorID': pd.Int64Dtype(),
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
    #parse_dates = ['lpep_pickup_datetime', 'lpep_dropoff_datetime']

    for f in files:
        url =f'{baseurl}{f}'

        df_ = pd.read_parquet(
            url, columns=taxi_dtypes.keys()  
            )
        #for col in parse_dates:
        #    df[col] = pd.to_datetime(df[col])
        df.append(df_)

    dfs = pd.concat(df, ignore_index=True)

    return dfs


