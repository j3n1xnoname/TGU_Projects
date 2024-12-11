import pandas as pd
from IPython.display import display, HTML

def analyze_dataframe(df):
    display(HTML("<strong>Первые несколько строк DataFrame</strong>"))
    display(df.head())
    print("-" * 160)

    display(HTML("<strong>Типы данных в каждом столбце</strong>"))
    display(df.dtypes)
    print("-" * 160)

    display(HTML("<strong>Количество пропущенных значений в каждом столбце</strong>"))
    display(df.isna().sum())
    print("-" * 160)

    display(HTML("<strong>Количество дубликатов в DataFrame</strong>"))
    display(df.duplicated().sum())
    print("-" * 160)

    display(HTML("<strong>Общая информацию о DataFrame</strong>"))
    display(df.info())
    print("-" * 160)