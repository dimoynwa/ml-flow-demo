from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.mlflow_demo.pipeline.prediction import PredictionPipeline
from src.mlflow_demo import logger

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_page():
    return render_template('index.html')

@app.route('/train', methods=['GET'])
def train():
    os.system('python main.py')
    return 'Training successfully.'

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            fixed_acidity = float(request.form['fixed_acidity'])
            volatile_acidity = float(request.form['volatile_acidity'])
            citric_acid = float(request.form['citric_acid'])
            residual_sugar = float(request.form['residual_sugar'])
            chlorides = float(request.form['chlorides'])
            free_sulfur_dioxide = float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide = float(request.form['total_sulfur_dioxide'])
            density = float(request.form['density'])
            pH = float(request.form['pH'])
            sulphates = float(request.form['sulphates'])
            alcohol = float(request.form['alcohol'])
            
            data = [fixed_acidity, volatile_acidity, citric_acid, residual_sugar, chlorides, free_sulfur_dioxide,
                    total_sulfur_dioxide, density, pH, sulphates, alcohol]
            data = np.array(data).reshape(1, 11)

            obj = PredictionPipeline()
            pred = obj.predict(data=data)

            logger.info(f'Predicted value for {data} is {pred}')

            return render_template('result.html', prediction=str(pred))
        except Exception as e:
            logger.error(f'Error prediction {e}')

if __name__ == '__main__':
    # app.run('0.0.0.0', port='8080', debug=True)
    app.run('0.0.0.0', port='8080')