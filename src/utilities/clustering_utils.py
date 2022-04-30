from IPython.display import display

from sqlite3 import DatabaseError
from matplotlib import pyplot as plt
from pandas import DataFrame
from sklearn.cluster import KMeans


def plot_kmeans_elbow(
        df: DataFrame, 
        max_n_clusters: int = 10, 
        max_iter: int = 1000
    ) -> None:
    """
    Displays the elbow plot
    """
    sse = {
        n_clusters: _get_inertia(df, n_clusters, max_iter)
        for n_clusters in range(1, max_n_clusters + 1)
    }
    plt.figure()
    plt.plot(sse.keys(), sse.values())
    plt.xlabel('Cluster count [k]')
    plt.show()


def _get_inertia(df: DataFrame, n_clusters: int, max_iter: int) -> list:
    """
    Returns the inertia value for a given kmeans model
    """
    kmeans = KMeans(n_clusters=n_clusters, max_iter=max_iter).fit(df)
    return kmeans.inertia_


def ordered_clustering(
        df: DataFrame,
        n_clusters: int,
        cluster_by_column_name: str, 
        ascending: bool
    ) -> DataFrame:
    """
    Returns a dataframe with ordered kmeans clusters
    based on the given column name
    """
    kmeans = KMeans(n_clusters=n_clusters)
    kmeans.fit(df[[cluster_by_column_name]])
    cluster_name = f'{cluster_by_column_name}_score'
    df[cluster_name] = kmeans.predict(df[[cluster_by_column_name]])
    target_score = (
        df.groupby(cluster_name)
            [cluster_by_column_name].mean()
            .reset_index()
            .sort_values(by=[cluster_by_column_name], ascending=ascending)
            .reset_index(drop=True)
                        )
    remap_clusters = {int(row[cluster_name]): idx for idx, row in target_score.iterrows()}
    df[cluster_name] = df[cluster_name].replace(remap_clusters)
    display(df.groupby(cluster_name)[cluster_by_column_name].describe())
    return df


