import numpy as np
from flask import Flask, request, jsonify, render_template
import pickle
import Project 
app = Flask(__name__)
model = pickle.load(open('model.pkl', 'rb'))
    
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',methods =["GET", "POST"])
def predict():
    '''
    For rendering results on HTML GUI'''
    
    if request.method == "POST":
       # getting input with name = fname in HTML form
       initial = request.form.get("initial")
       # getting input with name = lname in HTML form 
       final = request.form.get("final")                                       

    prediction = Project.inputPrediction(initial,final)
    df=prediction.tolist()
    text="The anomaly detection are:"
    normal="Normal Transactions: "+str(df[0])
    anomaly="Anomalous Transactions: "+str(df[1])
    return render_template('index.html',text=text,normal=normal,anomaly=anomaly)
if __name__ == "__main__":  
    app.run(debug=True)
    