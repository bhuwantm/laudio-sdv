import os

from sdv import Metadata
from sdv.relational import HMA1

from config import META_PATH
from core.tables.employee_sdv import EmployeesSDV
from core.tables.user_accounts_sdv import UserAccountsSDV

if __name__ == '__main__':
    # generate metadata which can be populated by each table module to build our relational metadata
    metadata = Metadata()

    # add employee tables detail in metadata
    employee_sdv = EmployeesSDV(metadata)
    employee_df, metadata = employee_sdv.get_df_and_metadata()

    # add user_accounts tables detail in metadata
    user_accounts_sdv = UserAccountsSDV(metadata)
    user_accounts_df, metadata = user_accounts_sdv.get_df_and_metadata()

    # map each table used in generating metadata to training data
    tables = {EmployeesSDV.TABLE_NAME: employee_df, UserAccountsSDV.TABLE_NAME: user_accounts_df}

    # train using HMA1 using metadata and tables as training data
    model = HMA1(metadata)
    model.fit(tables)
    new_data = model.sample(num_rows=10000)

    # get dataframe of employees and get its id column
    emp_id_list = new_data.get('employees')['id']

    # get dataframe of user_accounts and get its id column
    accounts_emp_id_list = new_data.get('user_accounts')['employee_id']

    print(len(emp_id_list), len(accounts_emp_id_list))

    # verify that all the employee_id in user_accounts is subset of employee table id set
    print(f'Account is Subset of employee: ', set(accounts_emp_id_list).issubset(emp_id_list))
    metadata.to_json(os.path.join(META_PATH, 'all.json'))
