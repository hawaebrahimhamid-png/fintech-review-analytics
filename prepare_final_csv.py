import pandas as pd

# Load Task 2 CSV
df = pd.read_csv("task2_results.csv")

# Create unique review IDs
df["review_id"] = range(1, len(df) + 1)

# Rename column
df = df.rename(columns={
    "review": "review_text"
})

# Ensure date format is correct
df["date"] = pd.to_datetime(df["date"]).dt.strftime("%Y-%m-%d")

# Select only required columns
df = df[
    [
        "review_id",
        "review_text",
        "rating",
        "date",
        "bank",
        "source",
        "sentiment_label",
        "sentiment_score",
        "identified_theme"
    ]
]

# Save final CSV
df.to_csv("data/final_reviews.csv", index=False)

print("Final CSV created successfully!")
