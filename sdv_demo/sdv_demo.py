import os

import pandas as pd
from sdv import Metadata
from sdv.relational import HMA1

from config import BASE_DIR

INPUT_CSV_PATH = os.path.join(BASE_DIR, 'sdv_demo', 'input_csv')
OUTPUT_CSV_PATH = os.path.join(BASE_DIR, 'sdv_demo', 'output_csv')


def run_sdv_demo():
    """
    demo function following all the necessary step for generating sample data using SDV
    :return: void
    """

    user_path = os.path.join(INPUT_CSV_PATH, 'users')
    sessions_path = os.path.join(INPUT_CSV_PATH, 'sessions')
    transactions_path = os.path.join(INPUT_CSV_PATH, 'transactions')

    # read csv using pandas as pandas dataframe
    user_df = pd.read_csv(user_path)
    sessions_df = pd.read_csv(sessions_path)
    transactions_df = pd.read_csv(transactions_path)

    # training data
    tables = {
        'users': user_df,
        'sessions': sessions_df,
        'transactions': transactions_df
    }

    # creating metadata for our tables
    metadata = Metadata()

    # adding users table to our metadata
    metadata.add_table(
        name='users',
        data=user_df,
        primary_key='user_id'
    )

    # adding sessions table having user_id as users foreign key
    metadata.add_table(
        name='sessions',
        data=sessions_df,
        primary_key='session_id',
        parent='users',
        foreign_key='user_id'
    )

    # describing field level metadata for timestamp
    # this will overwrite automatically generated corresponding field metadata
    transactions_fields = {
        'timestamp': {
            'type': 'datetime',
            'format': '%Y-%m-%d'
        }
    }

    # adding transactions table to our metadata with fields_metadata described above
    metadata.add_table(
        name='transactions',
        data=transactions_df,
        fields_metadata=transactions_fields,
        primary_key='transaction_id',
        parent='sessions'
    )

    # generating HMA1 model using our metadata
    model = HMA1(metadata)

    # fitting our training data to model
    model.fit(tables)

    # generating new sample data from our trained modal
    new_data = model.sample()
    print(new_data)
