"""
data_ingestion.py
Loads a dataset from disk into a pandas DataFrame, with basic validation.
"""

import pandas as pd
import os


def load_csv(filepath: str) -> pd.DataFrame:
    """
    Load a CSV file into a DataFrame.

    Args:
        filepath: path to the CSV file

    Returns:
        A pandas DataFrame with the loaded data

    Raises:
        FileNotFoundError: if the file doesn't exist
        ValueError: if the file is empty
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"No file found at: {filepath}")

    df = pd.read_csv(filepath)

    if df.empty:
        raise ValueError(f"File at {filepath} loaded but contains no data")

    print(f"Loaded {df.shape[0]} rows and {df.shape[1]} columns from {filepath}")
    return df


def get_basic_info(df: pd.DataFrame) -> dict:
    """
    Return a quick summary of a DataFrame: shape, column names, dtypes,
    and how many missing values are in each column.
    """
    info = {
        "num_rows": df.shape[0],
        "num_columns": df.shape[1],
        "columns": list(df.columns),
        "dtypes": df.dtypes.astype(str).to_dict(),
        "missing_values": df.isnull().sum().to_dict(),
    }
    return info


if __name__ == "__main__":
    # Quick manual test — run this file directly to check it works
    df = load_csv("data/sample.csv")
    info = get_basic_info(df)

    print("\n--- Dataset Info ---")
    print(f"Rows: {info['num_rows']}, Columns: {info['num_columns']}")
    print(f"Columns: {info['columns']}")
    print("\nMissing values per column:")
    for col, count in info['missing_values'].items():
        print(f"  {col}: {count}")