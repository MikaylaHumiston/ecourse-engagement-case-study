# ecourse-engagement-case-study
This project analyzes learner behavior on a digital course platform using Python, Power BI, and Databricks. The goal is to uncover actionable insights into user engagement and course completion patterns to support strategic product and content decisions.

## Project Objectives

- Explore learner engagement using activity and performance data
- Identify patterns associated with course completion
- Build dashboards in both Power BI and Databricks for stakeholder reporting
- Simulate a real-world data pipeline with Databricks features (notebooks, jobs, alerts, Unity Catalog, delta tables, etc)

## Tools Used

- **Python (pandas/matplotlib) & PySpark** (data cleaning, transformations, visualizations, modeling)
- **Jupyter Notebook** (functional presentation of python scripts/visualiatons)
- **Power BI Desktop** (interactive dashboard)
- **Databricks** (data ingestion, pipeline automation, governance, dashboard)

## Databricks Workflow

- Use Spark and delta tables to build a raw-to-clean (bronze-to-gold) pipeline
- Save raw, cleaned, and aggregated data as managed Delta tables
- Use Jobs for automating data management tasks
- Add alerts to monitor quality and completion trends

## Key Insights

- Completion rate/status is associated with number of videos watched/quizzes taken
- Quiz scores are generally stable across categories, but Science is slightly behind
- Mobile users are slightly less likely to complete courses than desktop users

## Next Steps

- Set up Databricks Jobs and Alerts to automate weekly insight delivery
-

## Note on Data

The dataset is synthetic and intended for educational and demonstration purposes. Source: [Kaggle – Predict Online Course Engagement Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-course-engagement-dataset)
