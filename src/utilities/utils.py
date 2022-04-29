from IPython.display import display
from pandas import DataFrame


def df_summarise(df: DataFrame) -> None:
    """
    Displays the summary of a given DataFrame
    """
    display(df.shape)
    display(df.columns)
    display(df.head())
