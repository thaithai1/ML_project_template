
import pandas as pd


def print_data(path):
    """
    Print the dataset corresponding to the path

    Parameters
    ----------
    path : str
        dataset path
    """
    df = pd.read_csv('../../data/raw/train.csv')
    print(df)


if __name__ == "__main__":
    path = '../../data/raw/train.csv'
    print_data(path)
