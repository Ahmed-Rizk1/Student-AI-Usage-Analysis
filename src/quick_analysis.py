
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os

def run_analysis():
    df = pd.read_csv("data/processed/cleaned_data.csv")
    
    print("Dataset Overview:")
    print(df.describe())
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    print("\nCorrelation Matrix:")
    numeric_df = df.select_dtypes(include=['float64', 'int64'])
    print(numeric_df.corr())
    
    print("\nKey Insights:")
    avg_improvement = df['grade_improvement'].mean()
    print(f"Average Grade Improvement: {avg_improvement:.2f}")
    
    users = df[df['uses_ai'] == 'Yes']
    non_users = df[df['uses_ai'] == 'No']
    
    print(f"Avg Grades After (AI Users): {users['grades_after_ai'].mean():.2f}")
    print(f"Avg Grades After (Non-Users): {non_users['grades_after_ai'].mean():.2f}")

if __name__ == "__main__":
    run_analysis()
