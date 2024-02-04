if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test
  
import pandas as pd   
import inflection

@transformer

def transform(data, *args, **kwargs): 
    
    print(f'Total rows :{data.shape[0]}')# print(len(data))
    print(f"Preprocessing:rows with 0 passengers: {data['passenger_count'].isin([0]).sum()}")
    print(f"Preprocessing:rows with 0 trip distance : {data['trip_distance'].isin([0]).sum()}")
    
    #print(f"Preprocessing:filtered data : {data[data['passenger_count'] > 0 |  data['trip_distance'] > 0].sum()}")
     
    data = data[(data['passenger_count'] != 0) & (data['trip_distance'] != 0)]
     
    data['lpep_pickup_date'] = pd.to_datetime(data['lpep_pickup_datetime'],unit='ms', errors='coerce')
    data['lpep_pickup_date'] =data['lpep_pickup_date'].dt.date
    data.columns = data.columns.map(inflection.underscore)
    return data
 
@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output.columns.__contains__('vendor_id'), 'column names are in snakecase'
@test
def test_output(output, *args) -> None:
    assert output['passenger_count'].isin([0]).sum()==0 , 'There are rides with zero passengers'

@test
def test_output(output, *args) -> None:
    assert output['trip_distance'].isin([0]).sum()==0 , 'There are rides with zero trip distance'