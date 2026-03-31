# Student Sleep & GPA Analysis - IT Tools Project

**College:** BIT Mesra Ranchi  
**Course:** MCA Second Semester  
**Subject:** IT Tools  

---

## Project Overview

This project analyzes the relationship between student sleep patterns and academic performance (CGPA). Using a real-world dataset of university students, it applies exploratory data analysis and a Machine Learning model (Linear Regression) to predict a student's GPA based on their daily habits.

The platform provides a comprehensive dashboard built using **Python** alongside **Flask** for the backend, and **HTML/CSS/JavaScript** coupled with **Plotly** for interactive data visualizations.

## Key Features

1. **Data Explorer**: Inspect raw data rows, view summary statistics (`df.describe()`), and analyze column data types straight from the processed dataset.
2. **GPA Predictor**: Leverage interactive sliders to adjust metrics such as Study Hours, Sleep Duration, Screen Time, Physical Activity, and Sleep Quality to see an instantly predicted GPA on a 1-10 scale.
3. **Interactive Analytics Charts**: 
   - Side-by-side bar charts mapping grades across genders.
   - Core habit importance bar chart demonstrating what impacts your GPA the most.
   - Comprehensive correlation heatmap mapping relationships among variables.

## Tech Stack

- **Backend:** Python, Flask, Pandas, NumPy, Scikit-Learn
- **Frontend:** HTML5, CSS3, Vanilla JavaScript, Plotly.js
- **Dataset:** `student_sleep_patterns.csv`

## Setup & Running Locally

1. **Install Dependencies:**
   Ensure you have Python installed. Then, install the required packages:
   ```bash
   pip install flask pandas numpy scikit-learn
   ```

2. **Run the Application:**
   Execute the main python script from the root directory:
   ```bash
   python app.py
   ```

3. **Access the Application:**
   Open your preferred web browser and navigate to: `http://127.0.0.1:8081`

## Project Team

- **Suraj Prakash Gautam** (MCA/10011/25)
- **Ram Hembrom** (MCA/10051/25)
- **Hash Malakar** (MCA/10010/25)
- **Krishu Kumar** (MCA/10014/25)
- **Raj Ranjan** (MCA/10072/25)
