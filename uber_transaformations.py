## mage data tranformer

import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """

    df['tpep_pickup_datetime']=pd.to_datetime(df['tpep_pickup_datetime'])
    df['tpep_dropoff_datetime']=pd.to_datetime(df['tpep_dropoff_datetime'])

    datetime_dim = df[['tpep_pickup_datetime','tpep_dropoff_datetime']].drop_duplicates().reset_index(drop=True)
    datetime_dim['datetime_id']=datetime_dim.index

    datetime_dim['pick_hour'] = datetime_dim['tpep_pickup_datetime'].dt.hour ## converting each value to datetime using .dt and then extracting hour using .hour
    datetime_dim['pick_weekday'] = datetime_dim['tpep_pickup_datetime'].dt.weekday
    datetime_dim['pick_day'] = datetime_dim['tpep_pickup_datetime'].dt.day
    datetime_dim['pick_month'] = datetime_dim['tpep_pickup_datetime'].dt.month
    datetime_dim['pick_year'] = datetime_dim['tpep_pickup_datetime'].dt.year
    
    datetime_dim['drop_hour'] = datetime_dim['tpep_dropoff_datetime'].dt.hour
    datetime_dim['drop_weekday'] = datetime_dim['tpep_dropoff_datetime'].dt.weekday
    datetime_dim['drop_day'] = datetime_dim['tpep_dropoff_datetime'].dt.day
    datetime_dim['drop_month'] = datetime_dim['tpep_dropoff_datetime'].dt.month
    datetime_dim['drop_year'] = datetime_dim['tpep_dropoff_datetime'].dt.year

    passenger_count_dim = df[['passenger_count']].drop_duplicates().reset_index(drop=True)
    passenger_count_dim['passenger_count_id'] = passenger_count_dim.index

    trip_distance_dim = df[['trip_distance']].drop_duplicates().reset_index(drop=True)
    trip_distance_dim['trip_distance_id'] = trip_distance_dim.index

    rate_code_dim = df[['RatecodeID']].drop_duplicates().dropna().reset_index(drop=True)
    rate_code_dim['rate_code_id'] = rate_code_dim.index
    dic = { 1: 'Standard rate',
        2: 'JFK',
        3: 'Newark',
        4: 'Nassau or Westchester',
        5: 'Negotiated fare',
        ##6: 'Group ride', depricated
        99: 'Group ride'}

    rate_code_dim['rate_code_name'] = rate_code_dim['RatecodeID'].map(dic)


    dic2 = {1: 'Credit card',
        2: 'Cash',
        3: 'No charge',
        4: 'Dispute',
        5: 'Unknown',
        6: 'Voided trip' 
    }
    payment_dim = pd.DataFrame(list(dic2.items()),columns=['payment_type','payment_type_name'])
    payment_dim['payment_id'] = payment_dim.index

    location_dim = df.apply(lambda x : x['PULocationID'] | x['DOLocationID'],axis=1).drop_duplicates().dropna().reset_index(drop=True)
    location_dim=pd.DataFrame(location_dim,columns=['location_type_name'])
    location_dim['location_id'] = location_dim.index

    fact_table = df.merge(datetime_dim, on=['tpep_pickup_datetime','tpep_pickup_datetime'])\
                    .merge(passenger_count_dim,on='passenger_count')\
                    .merge(payment_dim,on='payment_type')\
                    .merge(rate_code_dim,on='RatecodeID')\
                    .merge(trip_distance_dim,on='trip_distance')\
                    .merge(location_dim,left_on='PULocationID',right_on='location_type_name')\
                    .merge(location_dim,left_on='DOLocationID',right_on='location_type_name')\
                    [['VendorID','datetime_id','passenger_count_id','payment_id','rate_code_id','trip_distance_id','location_id_x','location_id_y',
                      'fare_amount','extra','mta_tax','tip_amount','tolls_amount','improvement_surcharge','total_amount','congestion_surcharge','Airport_fee']]

    fact_table.rename(columns={'location_id_x' : 'pickup_location_id',
                           'location_id_y':'dropoff_location_id'})
    
    return {'datetime_dim':datetime_dim.to_dict(orient='dict'),
            'passenger_count_dim':passenger_count_dim.to_dict(orient='dict'),
            'trip_distance_dim':trip_distance_dim.to_dict(orient='dict'),
            'rate_code_dim':rate_code_dim.to_dict(orient='dict'),
            'payment_dim':payment_dim.to_dict(orient='dict'),
            'location_dim':location_dim.to_dict(orient='dict'),
            'fact_table':fact_table.to_dict(orient='dict')}


    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
