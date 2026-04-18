from pathlib import Path
import pandas as pd

BASE_DIR = Path(__file__).resolve().parent.parent
RAW_PATH = BASE_DIR / "data" / "raw" / "yelp_academic_dataset_business.json"
OUT_PATH = BASE_DIR / "data" / "processed" / "restaurants_clean.csv"

def main():
    df = pd.read_json(RAW_PATH, lines=True)

    cols = [
        "business_id",
        "name",
        "city",
        "state",
        "categories",
        "stars",
        "review_count"
    ]
    df = df[cols]

    df = df.dropna(subset=["categories"])
    df = df.drop_duplicates(subset=["business_id"])

    df = df[df["categories"].str.contains("Restaurant", case=False, na=False)]

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(OUT_PATH, index=False)

    print("Dataset procesado guardado en:")
    print(OUT_PATH)
    print(f"Filas: {df.shape[0]}")
    print(f"Columnas: {df.shape[1]}")

if __name__ == "__main__":
    main()