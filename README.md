# Student AI Usage Analysis

## 📌 Project Overview
This project analyzes how Artificial Intelligence tools impact student performance. By examining data on study habits, AI tool usage, and grades, we identify trends and provide actionable business recommendations for educational institutions.

The project includes:
- **Data Cleaning & Processing Pipeline**
- **Exploratory Data Analysis (EDA)**
- **Interactive Streamlit Dashboard**
- **Business Insights Report**

## 📂 Project Structure
```
├── data/
│   ├── raw/                  # Original dataset
│   └── processed/            # Cleaned data for analysis
├── notebooks/
│   └── eda.ipynb            # Jupyter Notebook for deep-dive analysis
├── src/
│   ├── cleaning.py           # Data cleaning and feature engineering script
│   └── quick_analysis.py     # Script for generating summary statistics
├── dashboard/
│   └── app.py                # Streamlit Dashboard application
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## 🚀 How to Run

### 1. Setup Environment
```bash
pip install -r requirements.txt
```

### 2. Process Data
Clean the raw data and generate the processed file:
```bash
python src/cleaning.py
```

### 3. Launch Dashboard
Explore the interactive dashboard:
```bash
streamlit run dashboard/app.py
```

## 📊 Key Insights & Business Recommendations

### Findings
1.  **Positive Correlation**: Students using AI tools generally show an improvement in grades (`grades_after_ai` > `grades_before_ai`).
2.  **Tool Preference**: **Copilot** and **ChatGPT** are the most frequently used tools, particularly for **Coding** and **Homework**.
3.  **Study Efficiency**: There is a nuance in study hours; AI users might spend less time for the same or better results, indicating efficiency.

### Recommendations for Institutions
- **Integration, Not Ban**: Since AI correlates with performance improvement, schools should integrate AI literacy into usage policies rather than banning it.
- **Tool Licensing**: Consider institutional licenses for top tools (Copilot/Gemini) to ensure equitable access.
- **Curriculum Adaptation**: Shift focus from rote homework (easily automated) to critical thinking and complex problem-solving.

## 🛠 Technologies Used
- **Python**: Core language
- **Pandas**: Data manipulation
- **Streamlit**: Dashboard framework
- **Plotly**: Interactive visualizations
- **Seaborn/Matplotlib**: Static analysis

## 📬 Contact
Ready for deeper analysis? Feel free to fork this repo or reach out!
