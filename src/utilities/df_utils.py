from typing import Any
from IPython.display import display
from pandas import DataFrame


def df_summarise(df: DataFrame) -> None:
    """
    Displays the summary of a given DataFrame
    """
    display(df.shape)
    display(df.columns)
    display(df.head())


def aggregate(df: DataFrame, groupby_col: str) -> DataFrame:
    """
    Returns aggregated dataframe based on given column
    """
    agg_df = (df[[groupby_col, 'total_price']]
                .sort_values(by=groupby_col)
                .groupby(groupby_col)
                .agg(['count', 'sum', 'mean']))
    return agg_df


def show_stats(df: DataFrame, stats_column_name: str) -> None:
    """
    Displays given column stats and histogram
    """
    display(df[stats_column_name].describe())
    df[stats_column_name].plot.hist()


def get_zip_code_stem(zip_code: Any) -> str:
    """
    Returns zip code stem
    """
    return zip_code[:2] if str(zip_code).isnumeric() else zip_code
