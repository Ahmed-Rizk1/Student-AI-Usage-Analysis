import pandas as pd
import numpy as np
import os

def load_data(filepath):
    """
    Load data from CSV file.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found: {filepath}")
    return pd.read_csv(filepath)

def clean_data(df):
    """
    Clean the dataset:
    - Handle missing values
    - Remove duplicates
    - Standardize column names
    """
    # Standardize column names
    df.columns = [col.strip().lower().replace(' ', '_') for col in df.columns]

    # Remove duplicates
    df = df.drop_duplicates()

    # Handle missing values
    # For 'ai_tools_used' and 'purpose_of_ai', if 'uses_ai' is No, fill with 'None'
    # Check if 'uses_ai' column exists first to be safe
    if 'uses_ai' in df.columns:
        mask_no_ai = df['uses_ai'].astype(str).str.lower() == 'no'
        
        if 'ai_tools_used' in df.columns:
            df.loc[mask_no_ai, 'ai_tools_used'] = 'None'
            df['ai_tools_used'] = df['ai_tools_used'].fillna('None')
            
        if 'purpose_of_ai' in df.columns:
            df.loc[mask_no_ai, 'purpose_of_ai'] = 'None'
            df['purpose_of_ai'] = df['purpose_of_ai'].fillna('None')

    # For numeric columns, we might just drop rows with missing essential stats or fill with median
    # In this specific small dataset, we'll drop rows with missing numeric info if any, 
    # but based on initial view, it looks mostly clean. 
    # We will enforce numeric types.
    numeric_cols = ['age', 'study_hours_per_day', 'grades_before_ai', 'grades_after_ai', 'daily_screen_time_hours']
    for col in numeric_cols:
        if col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')
    
    # Drop rows where critical numeric usage data is missing
    df = df.dropna(subset=numeric_cols)

    return df

def feature_engineering(df):
    """
    Add new features for analysis.
    """
    # Grade improvement
    if 'grades_before_ai' in df.columns and 'grades_after_ai' in df.columns:
        df['grade_improvement'] = df['grades_after_ai'] - df['grades_before_ai']
    
    # AI Usage Category
    if 'uses_ai' in df.columns:
        df['user_category'] = df['uses_ai'].apply(lambda x: 'AI User' if x == 'Yes' else 'Non-User')

    return df

if __name__ == "__main__":
    # Test execution
    raw_path = os.path.join("data", "raw", "students_ai_usage.csv")
    if os.path.exists(raw_path):
        df = load_data(raw_path)
        df_clean = clean_data(df)
        df_final = feature_engineering(df_clean)
        
        out_path = os.path.join("data", "processed", "cleaned_data.csv")
        df_final.to_csv(out_path, index=False)
        print(f"Data cleaned and saved to {out_path}")
        print(f"Shape: {df_final.shape}")
    else:
        print("Raw data not found, skipping standalone run.")
