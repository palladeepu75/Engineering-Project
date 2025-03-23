from flask import Flask, render_template, request, jsonify
from sklearn.ensemble import RandomForestClassifier
import numpy as np
import joblib

# Load the pre-trained model
filename = 'bank_model.pkl'
lmodel = joblib.load(filename)

def predict_loan(Age, Income, Family, CCAvg, Education, Mortgage, Securities_Account, CD_Account):
    features = [[Age, Income, Family, CCAvg, Education, Mortgage, Securities_Account, CD_Account]]
    pred = lmodel.predict(features)
    target = int(pred[0])  # Convert NumPy array to int for JSON serialization
    return target

# Create Flask app
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/prediction')
def prediction_page():
    return render_template('prediction.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Parse JSON request
        
        Age = request.form['Age']
        Income = request.form['Income']
        Family = request.form['Family']
        CCAvg = request.form['CCAvg']
        Education = request.form['Education']
        Mortgage = request.form['Mortgage']
        Securities_Account = request.form['Securities']
        CD_Account = request.form['CD_Account']

        # Validate inpu

        # Make prediction
        result = predict_loan(Age, Income, Family, CCAvg, Education, Mortgage, Securities_Account, CD_Account)
        #return jsonify({"approval_prediction": result})
        result = 'Approved' if result == 1 else 'Rejected'
        return render_template('prediction.html', prediction_text='Approval Prediction: {}'.format(result))
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)