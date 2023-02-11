# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 15:23:24 2023

@author: admin
"""

import numpy as np
from flask import Flask, request, jsonify, render_template

import pickle


app = Flask(__name__)
model = pickle.load(open('/home/shikha683/LRDateFruit/Assignmentlinear.pkl','rb')) 


@app.route('/')
def home():
  
    return render_template("index.html")
  
@app.route('/predict',methods=['GET'])
def predict():
    
    
    '''
    For rendering results on HTML GUI
    '''

    
    area = float(request.args.get('area'))
    perimeter = float(request.args.get('perimeter'))
    prediction =int(model.predict([[area,perimeter]]))
    return render_template('index.html', prediction_text=prediction)


app.run()
