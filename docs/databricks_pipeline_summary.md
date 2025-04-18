# Databricks Pipeline Summary

This Databricks notebook implements a simple data engineering pipeline for the eCourse Engagement dataset.

## Bronze Table

- Source: `online_course_engagement_data.csv`
- Ingested with Spark CSV reader
- Stored as `bronze_ecourse_engagement` (Delta format)

## Silver Table

- Renamed columns to `snake_case`
- Added human-readable labels for:
  - `device_type` → `device_type_label`
  - `course_completion` → `course_completion_label`
- Stored as `silver_ecourse_engagement`

## Data Quality

- Checked for missing values
- Validated unique value counts
- Optional assertions and null filtering

## Alert

- SQL alert monitors `% of null quiz_scores`
- Trigger: null rate > 5%
- Configured via Databricks SQL Alert UI

## Notes

- Pipeline is manually triggered for now
- Data quality logic can be scaled into Delta Live Tables (DLT) or jobs
