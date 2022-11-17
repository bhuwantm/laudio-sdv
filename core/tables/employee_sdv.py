import os

import pandas as pd
import sdv
from sdv import Metadata

from config import INPUT_CSV_PATH
from core.base_sdv import BaseSDV


class EmployeesSDV(BaseSDV):
    TABLE_NAME = 'employees'

    def __init__(self, metadata: Metadata):
        super(EmployeesSDV, self).__init__(metadata)
        self.input_file = os.path.join(INPUT_CSV_PATH, 'employees.csv')

    def _get_df_csv(self) -> pd.DataFrame:
        df = pd.read_csv(self.input_file)
        return df

    @staticmethod
    def _get_fields_metadata() -> dict:
        fields_metadata = {
            'join_date': {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            'most_recent_hire_date': {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            "termination_date": {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            "first_name": {
                'type': 'categorical',
                'pii': True,
                'pii_category': 'first_name'
            },
            "middle_name": {
                'type': 'categorical',
            },
            "last_name": {
                'type': 'categorical',
                'pii': True,
                'pii_category': 'last_name'
            },
            "pay_level": {
                "type": "categorical"
            },
            "degree_level_id": {
                "type": "categorical"
            },
            "generation_id": {
                "type": "categorical"
            },
            "phone_work": {
                "type": "categorical"
            },
            "phone_cell": {
                "type": "categorical"
            },
            "phone_home": {
                "type": "categorical"
            },
            "profile_pic_link": {
                "type": "categorical"
            },
            "profile_pic_file_id": {
                "type": "numerical",
                "subtype": "integer"
            },
            "shift_id": {
                "type": "numerical",
                "subtype": "integer"
            },
            "manager_employee_id": {
                "type": "numerical",
                "subtype": "integer"
            },
            "available_pto_hours": {
                "type": "categorical"
            },
            "sso_username": {
                "type": "categorical"
            },
            "facility_id": {
                "type": "categorical"
            },
            'created_at': {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            'updated_at': {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            'anniversary_date': {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            'job_code_start_date': {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            'state_seniority_date': {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            }
        }
        return fields_metadata

    def get_df_and_metadata(self) -> [pd.DataFrame, sdv.Metadata]:
        df = self._get_df_csv()
        self.metadata.add_table(
            name=self.TABLE_NAME,
            data=df,
            primary_key='id',
            fields_metadata=self._get_fields_metadata(),
        )

        return df, self.metadata
