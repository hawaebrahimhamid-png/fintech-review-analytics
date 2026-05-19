import pandas as pd
from sqlalchemy import create_engine

# Load final CSV
df = pd.read_csv("data/final_reviews.csv")

# PostgreSQL connection
engine = create_engine(
    "postgresql+psycopg2://postgres:1234@localhost:5432/bank_reviews"
)

# Create unique banks table
banks = df[["bank"]].drop_duplicates()

banks["app_name"] = banks["bank"]

# Rename bank column
banks = banks.rename(columns={
    "bank": "bank_name"
})

# Insert into banks table
banks.to_sql(
    "banks",
    engine,
    if_exists="append",
    index=False
)

# Read banks with generated IDs
bank_df = pd.read_sql("SELECT * FROM banks", engine)

# Merge bank IDs into reviews
df = df.merge(bank_df, left_on="bank", right_on="bank_name")

# Select review columns
reviews = df[
    [
        "review_id",
        "bank_id",
        "review_text",
        "rating",
        "date",
        "sentiment_label",
        "sentiment_score",
        "identified_theme",
        "source"
    ]
]

# Rename date column
reviews = reviews.rename(columns={
    "date": "review_date"
})

# Insert reviews
reviews.to_sql(
    "reviews",
    engine,
    if_exists="append",
    index=False
)

print("Data inserted successfully!")