import pandas as pd

def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    cols = ["student_id", "age"]
    data = pandas.DataFrame(student_data,columns=cols)
    return data
