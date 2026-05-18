from flask import Flask, render_template, request
import os 
import numpy as np
import pandas as pd
from src.datascience.pipeline.prediction_pipeline import PredictionPipeline

# Initialize Flask App
app = Flask(__name__) 

# Route to Home page
@app.route('/',methods=['GET']) 
def homePage():
    return render_template("index.html")


# Route to model trainer page
@app.route('/train',methods=['GET']) 
def training():
    # Runs main.py file and trains model
    os.system("python main.py")
    return "Training Successful!" 

# Routes to predictions page
@app.route('/predict',methods=['POST','GET']) 
def index():
    if request.method == 'POST':
        try:
            #  Reading inputs
            fixed_acidity =float(request.form['fixed_acidity'])
            volatile_acidity =float(request.form['volatile_acidity'])
            citric_acid =float(request.form['citric_acid'])
            residual_sugar =float(request.form['residual_sugar'])
            chlorides =float(request.form['chlorides'])
            free_sulfur_dioxide =float(request.form['free_sulfur_dioxide'])
            total_sulfur_dioxide =float(request.form['total_sulfur_dioxide'])
            density =float(request.form['density'])
            pH =float(request.form['pH'])
            sulphates =float(request.form['sulphates'])
            alcohol =float(request.form['alcohol'])
       
            # Storing in the form of a list
            data = [fixed_acidity,volatile_acidity,citric_acid,residual_sugar,chlorides,free_sulfur_dioxide,total_sulfur_dioxide,density,pH,sulphates,alcohol]
            data = np.array(data).reshape(1, 11)
            
            # Prediction
            obj = PredictionPipeline()
            predict = obj.predict(data)

            # Convert prediction to integer
            prediction = int(round(predict[0]))

            # Keep prediction between 1 and 7
            prediction = max(1, min(prediction, 7))

            return render_template(
                'results.html',
                prediction=prediction
            )

        except Exception as e:
            print('The Exception message is: ',e)
            return 'something is wrong'

    else:
        return render_template('index.html')


if __name__ == "__main__":
	
	app.run(host="0.0.0.0", port = 8080)