from pathlib import Path
import pandas as pd


RAW_DIR = Path("data/raw")


def ingest_data():

    files = list(RAW_DIR.glob("*.csv"))

    print(f"Found {len(files)} datasets")

    for file in files:

        print("\n" + "="*70)
        print("Dataset:", file.name)

        df = pd.read_csv(file)

        print("Shape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nHead:")
        print(df.head())

        print("\nMissing Values:")
        print(df.isnull().sum())


if __name__ == "__main__":
    ingest_data()