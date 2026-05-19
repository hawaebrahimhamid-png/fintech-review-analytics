# Fintech Review Analytics

## Project Overview

This project analyzes customer reviews from Ethiopian mobile banking applications collected from the Google Play Store. The goal is to understand customer satisfaction, identify common issues, and extract actionable insights using data analysis, sentiment analysis, and thematic exploration.

The project focuses on three major Ethiopian banks:

- Commercial Bank of Ethiopia (CBE)
- Bank of Abyssinia (BOA)
- Dashen Bank

The analysis supports:
- Customer sentiment understanding
- Service improvement insights
- Data-driven decision-making in fintech applications

---

## Tools and Technologies Used

- Python
- Pandas
- Jupyter Notebook
- Google Play Scraper
- NLTK
- spaCy
- VADER Sentiment Analysis
- Transformers (Hugging Face)
- Scikit-learn
- Matplotlib
- Seaborn
- VS Code
- Git & GitHub

---

## Task 1: Data Collection and Preprocessing

### Scraping Methodology

Customer reviews were collected using the `google-play-scraper` library.

Steps:
1. Connected to Google Play Store
2. Extracted newest reviews for each banking app
3. Collected:
   - Review text
   - Rating
   - Review date
   - Bank name
   - Source platform
4. Cleaned dataset by:
   - Removing missing values
   - Removing duplicate reviews
5. Saved dataset as CSV file

Each bank contributed approximately 400 reviews, totaling around 1,200 reviews.

---

## Dataset Information

### Source
Google Play Store

### Banks Included
- CBE Mobile Banking
- BOA Mobile Banking
- Dashen Super App

### Date Range
May 2026 (latest available reviews during scraping)

### Dataset Size
~1,200 reviews

---

## Dataset Structure

| Column Name | Description |
|-------------|-------------|
| review | Customer feedback text |
| rating | User rating (1–5) |
| date | Review submission date |
| bank | Bank name |
| source | Data source (Google Play Store) |

---

## Task 2: Sentiment and Thematic Analysis

### Objective

To analyze customer emotions and extract common themes from mobile banking app reviews.

---

## Methodology

### 1. Data Preprocessing
- Converted text to lowercase
- Removed punctuation and special characters
- Removed stopwords
- Tokenized using spaCy
- Normalized review text

---

### 2. Sentiment Analysis
- Used VADER sentiment analysis model
- Classified reviews into:
  - Positive
  - Neutral
  - Negative
- Computed sentiment distribution per bank

---

### 3. Thematic Analysis
Identified recurring themes in customer feedback:

- Transaction failures
- Login/authentication issues
- App performance problems
- User experience feedback
- Positive service satisfaction

---

## Key Findings

- Transaction failures are the most common complaint
- Login issues significantly affect user satisfaction
- Positive reviews highlight convenience and usability
- BOA and CBE show higher negative sentiment compared to Dashen
- App performance issues are consistent across all banks

---

## Visualizations

The following analyses were performed:
- Sentiment distribution charts
- Rating vs sentiment comparison
- Bank-wise sentiment breakdown
- Most frequent keywords in reviews

---

## Limitations

- Dataset is limited to Google Play Store reviews only
- Some reviews contain slang and mixed languages
- VADER may not fully capture local linguistic context
- No iOS App Store data included

---

## Future Work

- Implement BERT-based sentiment analysis for higher accuracy
- Add Amharic language NLP support
- Expand dataset with App Store reviews
- Build interactive dashboard for monitoring trends
- Perform time-series sentiment tracking

---

## Project Structure

```
fintech-review-analytics/
│
├── data/
│   └── raw/
│       └── bank_reviews.csv
│
├── notebooks/
│   ├── eda.ipynb
│   └── task2_sentiment_analysis.ipynb
│
├── scripts/
│   └── scrape_reviews.py
│
├── src/
├── tests/
├── requirements.txt
└── README.md
```

------

## Task 3: PostgreSQL Data Storage

### Objective

To design and implement a relational PostgreSQL database to store cleaned and processed fintech review data for efficient querying and structured analysis.

---

## Database Setup

A PostgreSQL database named:

```
bank_reviews
```

was created to store the processed dataset.

---

## Schema Design

Two relational tables were created:

---

### 1. Banks Table

Stores metadata about each bank.

| Column      | Type              | Description                     |
|-------------|-------------------|---------------------------------|
| bank_id     | SERIAL PRIMARY KEY | Unique identifier              |
| bank_name   | VARCHAR(100)       | Name of the bank               |
| app_name    | VARCHAR(150)       | Mobile banking app name        |

---

### 2. Reviews Table

Stores cleaned review and sentiment data.

| Column              | Type              | Description                                      |
|---------------------|------------------|--------------------------------------------------|
| review_id           | TEXT PRIMARY KEY  | Unique review identifier                         |
| bank_id             | INTEGER (FK)      | Links to banks table                             |
| review_text         | TEXT              | Customer review text                             |
| rating              | INTEGER           | Star rating (1–5)                                |
| review_date         | DATE              | Date of review                                   |
| sentiment_label     | VARCHAR(20)       | Positive / Neutral / Negative                    |
| sentiment_score     | FLOAT             | Sentiment confidence score                       |
| identified_theme    | VARCHAR(100)      | Extracted theme (UI, transaction issues, etc.)   |
| source              | VARCHAR(50)       | Data source (Google Play Store)                  |

---

## Data Insertion Process

- Cleaned dataset (`final_reviews.csv`) was loaded using Python (Pandas)
- Database connection established using **SQLAlchemy** and **psycopg2**
- Data inserted into PostgreSQL using automated scripts
- Foreign key relationships maintained between **banks** and **reviews** tables

---

## Verification Queries

### Total Reviews

```sql
SELECT COUNT(*) FROM reviews;
```

Result:
```
913 reviews inserted successfully
```

---

### Bank-wise Data Check

```sql
SELECT * FROM banks;
```

---

### Sample Review Data

```sql
SELECT * FROM reviews LIMIT 5;
```

---

### Join Verification (Relational Integrity)

```sql
SELECT r.review_text, b.bank_name
FROM reviews r
JOIN banks b ON r.bank_id = b.bank_id;
```

---

## Key Outcomes

- Designed a relational database schema for fintech reviews
- Inserted 900+ cleaned review records
- Established proper foreign key relationships
- Enabled structured SQL-based analysis
- Demonstrated full data engineering pipeline (scraping → cleaning → storage)

---

## Tools Used in Task 3

- PostgreSQL
- SQL (DDL & DML)
- Python (psycopg2, SQLAlchemy)
- Pandas
- pgAdmin 4

---

## Conclusion (Task 3)

This task demonstrates how raw scraped data can be transformed into a structured relational database. The PostgreSQL implementation enables scalable storage, efficient querying, and future integration with analytics dashboards or machine learning pipelines.

---

# Task 4: Insights and Recommendations

## Objective

The objective of Task 4 was to transform sentiment and thematic analysis results into actionable business insights for Ethiopian mobile banking applications. The analysis focused on identifying customer satisfaction drivers, recurring pain points, cross-bank performance differences, and practical recommendations for improving mobile banking services.

---

## Methodology

Task 4 was built on outputs generated from previous tasks, including cleaned review data, sentiment labels, sentiment scores, and identified themes.

### Analytical Steps

1. Aggregated sentiment distribution across banks
2. Compared average ratings and sentiment scores
3. Identified recurring positive and negative themes
4. Generated visualizations for comparative analysis
5. Extracted business insights and recommendations

---

## Visualizations Created

The following visualizations were developed using Matplotlib and Seaborn:

- Sentiment Distribution by Bank
- Rating Distribution Across Banks
- Top Themes per Bank
- Sentiment Heatmap
- Sentiment Trend Over Time

These visualizations helped identify customer satisfaction patterns and operational weaknesses across the three banking applications.

---

## Satisfaction Drivers

### CBE
- Positive reviews highlighted reliable transaction performance and acceptable user experience.
- Customers appreciated successful banking operations and accessibility.

### BOA
- BOA received the strongest positive feedback regarding UI & Design.
- Users valued the application's usability and transaction efficiency.

### Dashen
- Dashen users frequently praised interface simplicity and navigation.
- Positive reviews also emphasized transaction functionality.

---

## Pain Points

### CBE
- Negative feedback revealed unresolved technical issues and customer support concerns.
- Some users experienced usability and transaction-related problems.

### BOA
- Customers reported interface inconsistencies and authentication-related complaints.
- Some reviews highlighted delays in issue resolution.

### Dashen
- Dashen showed the highest concentration of UI & Design complaints.
- Users also reported transaction delays and account access issues.

---

## Cross-Bank Comparison

- BOA achieved the strongest overall customer sentiment, driven mainly by positive UI and usability feedback.
- Dashen recorded the highest concentration of UI-related complaints, indicating usability and interface consistency challenges.
- CBE demonstrated relatively balanced transaction-related feedback but showed broader unresolved customer concerns.
- Transaction reliability and application stability emerged as recurring industry-wide issues across all banks.

---

## Recommendations

### CBE
- Improve customer support responsiveness.
- Reduce transaction-related technical failures.
- Enhance issue-resolution workflows for failed operations.

### BOA
- Improve interface consistency across app versions and devices.
- Strengthen authentication reliability.
- Enhance customer support efficiency.

### Dashen
- Redesign problematic UI workflows.
- Improve application stability during peak usage periods.
- Optimize backend transaction performance.

### Industry-Wide Recommendation
All banks should prioritize:
- Transaction reliability
- Application stability
- Authentication performance
- Faster customer support systems

---

## Tools Used in Task 4

- Python
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook

---

## Conclusion (Task 4)

Task 4 demonstrated how customer feedback can be transformed into actionable business intelligence using sentiment analysis, thematic exploration, and data visualization techniques.

The findings revealed that usability, transaction reliability, and application stability are the major factors influencing customer satisfaction in Ethiopian mobile banking applications. While each bank demonstrated strengths in specific areas, recurring complaints regarding failed transactions, login problems, and inconsistent user experiences highlight important opportunities for service improvement.

The recommendations generated from this analysis can support data-driven product enhancement and improved customer experience strategies within the fintech sector.

---

## Author

Hawa Ebrahim Hamid

---


## Conclusion

This project demonstrates an end-to-end fintech data analytics pipeline, starting from data collection to structured storage, analysis, and business insight generation.

In **Task 1**, customer reviews were scraped from Google Play Store, cleaned, and structured into a usable dataset containing approximately 1,200 reviews from three Ethiopian banks.

In **Task 2**, sentiment analysis and thematic analysis were performed to understand customer opinions. Reviews were classified into positive, neutral, and negative sentiments, and key issues such as transaction failures, login problems, and app performance were identified.

In **Task 3**, a relational PostgreSQL database was designed and implemented to store cleaned and processed data. The database enables efficient querying, structured analysis, and supports future scalability for dashboards and machine learning applications.

In **Task 4**, sentiment findings and thematic patterns were transformed into business-actionable insights through comparative analysis and visualization techniques. The analysis identified key customer satisfaction drivers, major pain points, and operational weaknesses across the banking applications. Practical recommendations were proposed to improve transaction reliability, application stability, authentication performance, and customer support efficiency.

Overall, this project provides valuable insights into customer satisfaction in Ethiopian mobile banking systems and demonstrates practical skills in data engineering, natural language processing, database management, and business analytics. The findings can help financial institutions improve service quality, optimize digital banking experiences, and support data-driven decision-making within the fintech sector.