import pandas as pd

def csv_to_parquet(csv_path: str, parquet_path: str):
    df = pd.read_csv(csv_path)
    df.to_parquet(parquet_path, engine="pyarrow", compression="snappy")

if __name__ == "__main__":
    csv_to_parquet("input.csv", "output.parquet")
