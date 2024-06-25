import pandas as pd
import numpy as np


def modifySalaryColumn(employees: pd.DataFrame) -> pd.DataFrame:
    def double(x):
        return np.multiply(x, 2)
    
    salary_column = employees["salary"]
    employees["salary"] = salary_column.apply(double)
    return employees
