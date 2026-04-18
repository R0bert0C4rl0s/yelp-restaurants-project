# Yelp Restaurants Project

This project builds a restaurant dataset from the Yelp business file for later clustering, recommendation, and graph analysis.

## Structure

- `data/raw/`: raw files
- `data/processed/`: cleaned outputs
- `src/`: reproducible scripts
- `notebooks/`: exploratory notebooks
- `reports/`: milestone reports

## How to run

1. Place `yelp_academic_dataset_business.json` in `data/raw/`
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
3. Build the processed dataset:
    python src/build_dataset.py