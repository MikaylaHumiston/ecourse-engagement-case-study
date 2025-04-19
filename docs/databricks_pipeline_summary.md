# Databricks Pipeline Summary

This Databricks notebook implements a simple data engineering pipeline for the eCourse Engagement dataset.

## Bronze Table

- Source: `online_course_engagement_data.csv`
- Ingested with Spark CSV reader
- Stored as `bronze_ecourse_engagement` (Delta format)

## Silver Table

- Renamed columns using snake case
- Added labels for readability:
  - `device_type` to `device_type_label` (0 = Desktop, 1 = Mobile)
  - `course_completion` to `course_completion_label` (0 = Not Completed, 1 = Completed)
- Stored as `silver_ecourse_engagement`

## Data Quality

- Check for missing values
- Validate unique value counts
- Check for invalid values (ex: negative values for quiz_score)

## Alert

- SQL alert monitors null or invalid quiz_score values
- Trigger: null rate > 5%
-

## Notes

- Pipeline is manually triggered for now
- Data quality maintenance can be built into Delta Live Tables or jobs
