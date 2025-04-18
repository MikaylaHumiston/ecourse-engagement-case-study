import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/online_course_engagement_data.csv")

# Display basic info
print("Shape of the dataset:", df.shape)
print("\nColumn Names:\n", df.columns)
print("\nFirst 5 Rows:\n", df.head())

# Check for missing values
print("\nMissing Values:\n", df.isnull().sum())

# Check data types
print("\nData Types:\n", df.dtypes)

# Descriptive stats
print("\nDescriptive Stats:\n", df.describe(include='all'))

# Unique values in each column
print("\nUnique Values per Column:\n")
for col in df.columns:
    print(f"{col}: {df[col].nunique()} unique values")

# Renaming columns in snake case
df.rename(columns = {
    "UserID": "User_ID",
    "CourseCategory": "Course_Category",
    "TimeSpentOnCourse": "Time_Spent_On_Course",
    "NumberOfVideosWatched": "Number_Of_Videos_Watched",
    "NumberOfQuizzesTaken": "Number_Of_Quizzes_Taken",
    "QuizScores": "Quiz_Scores",
    "CompletionRate": "Completion_Rate",
    "DeviceType": "Device_Type",
    "CourseCompletion": "Course_Completion"
}, inplace=True)

# Add new categorical labels without converting data types
df['Device_Type_Label'] = df['Device_Type'].map({0: 'Desktop', 1: 'Mobile'})
df['Course_Completion_Label'] = df['Course_Completion'].map({0: 'Not Completed', 1: 'Completed'})

# Check label mapping
print("\nLabel mapping check:\n", df[['Device_Type', 'Device_Type_Label', 'Course_Completion', 'Course_Completion_Label']].head())

# Average course completion by device type
device_summary = df.groupby('Device_Type_Label')['Completion_Rate'].mean()
print("\nAverage Completion Rate by Device:\n", device_summary)

# Average number of videos watched by course category
video_summary = df.groupby('Course_Category')['Number_Of_Videos_Watched'].mean()
print("\nAverage Number of Videos Watched by Course Category:\n", video_summary)
# Save cleaned version
df.to_csv("data/clean/online_course_engagement_data_cleaned.csv", index=False)
print("\nCleaned data saved to data/clean/")