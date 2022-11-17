import os

import pandas as pd
import sdv
from sdv import Metadata

from config import INPUT_CSV_PATH
from core.base_sdv import BaseSDV
from core.tables.employee_sdv import EmployeesSDV


class UserAccountsSDV(BaseSDV):
    TABLE_NAME = 'user_accounts'
    EMPLOYEE_FK_NAME = 'employee_id'

    def __init__(self, metadata: Metadata):
        super(UserAccountsSDV, self).__init__(metadata)
        self.input_file = os.path.join(INPUT_CSV_PATH, 'user_accounts.csv')

    def _get_df_csv(self) -> pd.DataFrame:
        df = pd.read_csv(self.input_file)
        return df

    @staticmethod
    def _get_fields_metadata() -> dict:
        fields_metadata = {
            "employee_id": {
                "type": "id",
                "subtype": "integer"
            },
            "last_password_changed_date": {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            "created_at": {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            },
            "updated_at": {
                'type': 'datetime',
                'format': '%Y-%m-%d'
            }
        }
        return fields_metadata

    def _add_relationship(self) -> None:
        self.metadata.add_relationship(
            EmployeesSDV.TABLE_NAME,
            self.TABLE_NAME,
            self.EMPLOYEE_FK_NAME
        )

    def get_df_and_metadata(self) -> [pd.DataFrame, sdv.Metadata]:
        df = self._get_df_csv()
        self.metadata.add_table(
            name=self.TABLE_NAME,
            data=df,
            primary_key='id',
            fields_metadata=self._get_fields_metadata()
        )
        self._add_relationship()
        return df, self.metadata
