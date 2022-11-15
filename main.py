from sdv import Metadata
from sdv.relational import HMA1

from core.employees.employee_sdv import EmployeesSDV

if __name__ == '__main__':
    metadata = Metadata()
    employee_sdv = EmployeesSDV(metadata)
    df, employee_metadata = employee_sdv.get_df_and_metadata()

    tables = {
        EmployeesSDV.TABLE_NAME: df
    }

    model = HMA1(employee_metadata)
    model.fit(tables)
    new_data = model.sample()
    print(new_data)
    print('Run Completed')
