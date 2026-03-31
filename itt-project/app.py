import pandas as pd
import numpy as np
from flask import Flask, render_template, request, jsonify
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# --- STEP 1: PREPARE OUR DATA & AI MODEL ---
def get_ready():
    df = pd.read_csv('student_sleep_patterns.csv')
    
    # Encode categorical columns
    df = pd.get_dummies(df, columns=['University_Year'], drop_first=True)

    # Create the CGPA (1 to 10 scale)
    np.random.seed(42)
    df['CGPA'] = (
        (df['Study_Hours'] * 0.3) + 
        (df['Sleep_Quality'] * 0.4) + 
        (df['Physical_Activity'] * 0.01) - 
        (df['Screen_Time'] * 0.1) + 
        2.5 + # Base 
        np.random.normal(0, 0.2, size=len(df))
    ).clip(1.0, 10.0)
    
    # Create "Grade" column from CGPA for the requested charts
    def assign_grade(cgpa):
        if cgpa >= 9.0: return 'A+'
        if cgpa >= 8.0: return 'A'
        if cgpa >= 7.0: return 'B'
        if cgpa >= 6.0: return 'C'
        if cgpa >= 5.0: return 'D'
        return 'F'
    
    df['Grade'] = df['CGPA'].apply(assign_grade)
    
    # Choose our features (numeric only, excluding ID, CGPA, Grade, Gender)
    exclude = {'Student_ID', 'CGPA', 'Grade', 'Gender'}
    features = [c for c in df.columns if c not in exclude and df[c].dtype in [np.float64, np.int64, bool]]
    model = LinearRegression().fit(df[features], df['CGPA'])
    
    return model, df, features

model, full_df, feature_names = get_ready()

# Core habit features (used for prediction sliders & focused analytics)
CORE_FEATURES = ['Study_Hours', 'Sleep_Duration', 'Screen_Time', 'Physical_Activity', 'Sleep_Quality']

# --- ROUTES ---
@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def calculate_gpa():
    data = request.json
    try:
        # Map slider inputs to their column names
        slider_map = {
            'Study_Hours': float(data['study']),
            'Sleep_Duration': float(data['sleep']),
            'Screen_Time': float(data['screen']),
            'Physical_Activity': float(data['physical']),
            'Sleep_Quality': float(data['quality']),
        }
        # Build full feature vector matching training columns (default 0 for encoded cols)
        row = {f: slider_map.get(f, 0) for f in feature_names}
        # Fill remaining numeric fields with dataset medians
        for f in feature_names:
            if f not in slider_map and f not in row:
                row[f] = full_df[f].median()
        input_vec = [[row[f] for f in feature_names]]
        prediction = model.predict(input_vec)[0]
        final_result = round(min(max(prediction, 1.0), 10.0), 2)
        return jsonify({'prediction': f"{final_result}"})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/explore')
def data_sample():
    return jsonify({
        'head': full_df.head().to_dict(orient='records'),
        'shape': full_df.shape,
        'describe': full_df.describe().round(2).reset_index().to_dict(orient='records'),
        'info': [{'column': c, 'type': str(full_df[c].dtype)} for c in full_df.columns]
    })

@app.route('/analytics')
def detailed_charts():
    # 1. Prepare Grade vs Gender data (Bar Chart)
    # Grouping into counts for Female and Male
    grade_order = ['A+', 'A', 'B', 'C', 'D', 'F']
    counts = full_df.groupby(['Grade', 'Gender']).size().unstack(fill_value=0)
    
    # Ensure all grades are present in the correct order
    for g in grade_order:
        if g not in counts.index:
            counts.loc[g] = 0
    counts = counts.reindex(grade_order)
    
    # 2. Gender distribution (Pie Chart)
    gender_counts = full_df['Gender'].value_counts()
    
    # 3. Importance & Heatmap — use only the 5 core habit features for clarity
    corr = full_df[CORE_FEATURES + ['CGPA']].corr().round(2)
    coef_map = dict(zip(feature_names, model.coef_))
    importance = {f: round(abs(coef_map.get(f, 0)), 3) for f in CORE_FEATURES}
    
    return jsonify({
        'grade_gender': {
            'labels': list(counts.index),
            'female': counts['Female'].tolist() if 'Female' in counts.columns else [0]*6,
            'male': counts['Male'].tolist() if 'Male' in counts.columns else [0]*6
        },
        'gender_dist': {
            'labels': list(gender_counts.index),
            'values': gender_counts.tolist()
        },
        'importance': {'labels': list(importance.keys()), 'values': list(importance.values())},
        'heatmap': {'labels': list(corr.columns), 'z': [list(row) for row in corr.values]}
    })

if __name__ == '__main__':
    print("🚀 Final ITT Project Hub starting at http://127.0.0.1:8081")
    app.run(debug=True, port=8081)
