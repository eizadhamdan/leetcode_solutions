import pandas as pd

def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
    pivot_df = weather.pivot_table(index="month", columns="city", values="temperature", aggfunc="max")
    return pivot_df

# import pandas as pd

# def pivotTable(weather: pd.DataFrame) -> pd.DataFrame:
#     pivot_df = weather.pivot_table(index="month", columns="city", values="temperature")
#     return pivot_df
