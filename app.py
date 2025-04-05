from flask import Flask, render_template, request
import joblib
import pandas as pd
import json

app = Flask(__name__)

# Load trained model pipeline and column metadata
pipeline = joblib.load('loan_approval_pipeline.pkl')

with open('feature_columns.json', 'r') as f:
    feature_columns = json.load(f)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get form input and convert to DataFrame
        form_data = request.form.to_dict()
        input_data = pd.DataFrame([form_data])

        # Convert numerical fields
        for col in feature_columns['numerical']:
            if col in input_data.columns:
                input_data[col] = pd.to_numeric(input_data[col])

        # Make prediction
        prediction = str(pipeline.predict(input_data)[0])
        probability = pipeline.predict_proba(input_data)[0][1]

        # Render result
        return render_template('index.html',
                               prediction=prediction,
                               probability=f"{probability*100:.2f}%",
                               show_result=True)

    except Exception:
        return render_template('index.html',
                               prediction="Error",
                               error_message="An error occurred. Please try again later.",
                               show_result=True)

if __name__ == '__main__':
    app.run(debug=True)
