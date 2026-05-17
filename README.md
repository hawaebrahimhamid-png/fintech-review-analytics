## Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian mobile banking applications collected from Google Play Store. The objective is to understand customer satisfaction, identify common issues, and extract insights from user feedback using data analysis and sentiment analysis techniques.

The project focuses on three Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The collected reviews will later be used for:
- Exploratory Data Analysis (EDA)
- Sentiment Analysis
- Correlation Analysis
- Financial service improvement insights

---

## Tools and Technologies Used

- Python
- Pandas
- Jupyter Notebook
- Google Play Scraper
- Matplotlib
- Seaborn
- Git & GitHub
- VS Code

---

## Scraping Methodology

Customer reviews were collected using the `google-play-scraper` Python package.

The scraping process:
1. Connected to Google Play Store
2. Retrieved newest reviews from each banking application
3. Extracted:
   - Review text
   - Rating
   - Review date
   - Bank name
   - Source platform
4. Cleaned the dataset by:
   - Removing missing values
   - Removing duplicate reviews
5. Saved the cleaned dataset as CSV

Each bank contributed approximately 400 reviews.

---

## Dataset Information

### Source
Google Play Store

### Banks Included
- CBE Mobile Banking
- BOA Mobile Banking
- Dashen Super App

### Date Range
The dataset contains the most recent reviews available during scraping in May 2026.

### Total Records
Approximately 1,200 reviews.

---

## Dataset Structure

| Column Name | Description |
|-------------|-------------|
| review | Customer review text |
| rating | User rating (1–5) |
| date | Review submission date |
| bank | Bank name |
| source | Review platform source |

---

## Project Structure

```bash
fintech-review-analytics/
│
├── data/
│   └── raw/
│       └── bank_reviews.csv
│
├── notebooks/
│   └── eda.ipynb
│
├── scripts/
│   └── scrape_reviews.py
│
├── src/
├── tests/
├── requirements.txt
└── README.md
```

---

## Limitations

- Reviews are limited to publicly available Google Play Store data.
- Some reviews may contain spelling mistakes or mixed languages.
- The dataset reflects user opinions only during the scraping period.
- App Store (iOS) reviews were not included.

---

## Future Work

- Perform sentiment analysis
- Build visual dashboards
- Analyze rating trends
- Compare customer satisfaction across banks
- Identify common banking service complaints

---

## Author

Hawa Ebrahim Hamid