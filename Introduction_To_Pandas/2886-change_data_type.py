import pandas as pd
import numpy as np

def changeDatatype(students: pd.DataFrame) -> pd.DataFrame:
    def convert(x):
        return int(x)

    grade_column = students["grade"]
    new_column = grade_column.apply(convert)
    students["grade"] = new_column
    return students
