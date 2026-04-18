# Week 3 Report – Yelp Restaurants Project

## 1. Project Proposal

### Domain
Local businesses, focused on restaurants.

### Problem Statement
Users face many restaurant options and need mechanisms to discover similar restaurants or identify relevant options efficiently.

### Expected Product Question
Which restaurants are similar to each other, and which restaurants should be recommended?

### Why this dataset is suitable
The Yelp business dataset contains restaurant metadata such as categories, rating, location, and review volume. This supports later stages of the course including feature engineering, clustering, recommendation, and graph analysis.

## 2. Source Inventory

- Source name: Yelp Open Dataset
- Source URL: https://www.kaggle.com/datasets/yelp-dataset/yelp-dataset
- Access conditions: public academic/open dataset
- Raw file used: yelp_academic_dataset_business.json
- Raw format: line-delimited JSON
- Estimated size: 116,078 KB

## 3. Schema Draft

Main entity table: businesses

Fields:
- business_id (primary key)
- name
- city
- state
- categories
- stars
- review_count

Expected role in the project:
This table is the catalog layer of the system and will be used as the basis for restaurant representation and later similarity/recommendation tasks.

Future possible joins:
- reviews via business_id
- tips via business_id

## 4. Processed Dataset V1

A first processed dataset was created from the Yelp business file.

Processing steps:
1. Load the raw business JSON file.
2. Keep only relevant columns.
3. Remove rows with missing categories.
4. Remove duplicate business_id values.
5. Filter businesses whose categories contain the word "Restaurant".
6. Save the cleaned table to data/processed/restaurants_clean.csv


## 5. Data Dictionary Draft

| Column         | Type   | Description                              |
|----------------|--------|------------------------------------------|
| business_id    | string | Unique restaurant identifier             |
| name           | string | Restaurant name                          |
| city           | string | City where the restaurant is located     |
| state          | string | State where the restaurant is located    |
| categories     | string | Yelp category labels                     |
| stars          | float  | Average Yelp star rating                 |
| review_count   | int    | Total number of reviews                  |

## 6. Scale Analysis

- Rows: 52286
- Columns: 7
- Missingness:
business_id     0
name            0
city            0
state           0
categories      0
stars           0
review_count    0
- Memory/sparsity note:
  This first processed table is compact and manageable for a single-student workflow. It is suitable as a base for future feature engineering and clustering tasks.

## 7. Ethics and Access Note

The dataset comes from the Yelp Open Dataset, which is publicly available for academic and analytical use. At this stage, the project uses only business-level information and does not rely on sensitive personal identifiers. The dataset is used only for educational purposes, and the workflow documents source provenance and processing decisions clearly.

## 8. Reproducibility

Command used to build the processed dataset:

```bash
python src/build_dataset.py