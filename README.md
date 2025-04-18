# ecourse-engagement-case-study
This project analyzes learner behavior on a digital course platform using Python, Power BI, and Databricks. The goal is to uncover actionable insights into user engagement and course completion patterns to support strategic product and content decisions.

## Project Objectives

- Explore learner engagement using behavioral and performance data
- Identify patterns in course completion, quiz scores, and device usage
- Build dashboards for stakeholder reporting and strategy
- Simulate a real-world data pipeline with Databricks features

## Tools Used

- **Python + Jupyter Notebook** (data cleaning, feature engineering, ML modeling)
- **Power BI Desktop** (interactive dashboard development)
- **Databricks** (data ingestion, pipeline automation, governance)

## Project Structure

| Folder       | Description |
|--------------|-------------|
| `/notebooks` | Python notebook and Databricks pipeline steps |
| `/powerbi`   | Dashboard screenshots (overview, behavior, devices) |
| `/data`      | Cleaned CSV used for Power BI input |
| `/docs`      | Project summary slides or PDF export (optional) |

## Key Insights

- Completion rates are strongly associated with videos watched and quizzes taken
- Quiz scores are generally stable across categories, but Science lags slightly
- Mobile users are slightly less likely to complete courses than desktop users

## Next Steps

- Add anomaly detection to flag low-performing course categories
- Deploy dashboards on a shared workspace or internal portal
- Set up Databricks Jobs and Alerts to automate weekly insight delivery

## Note on Data

The dataset is **synthetic** and used for educational and demonstration purposes. Source: [Kaggle – Predict Online Course Engagement Dataset](https://www.kaggle.com/datasets/rabieelkharoua/predict-online-course-engagement-dataset)
