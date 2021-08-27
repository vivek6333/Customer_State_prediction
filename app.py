# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:06:01 2019

@author: prithvi
"""
import flask
from flask import Flask, request , jsonify, render_template
#import jinja2
import numpy as np
import pandas as pd
import pickle

from flask import Flask, request,jsonify,render_template
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)
filename = 'Model_Gb.pickle'
model = pickle.load(open(filename, 'rb'))

@app.route('/')
def man():
    return render_template('home.html')


@app.route('/predict', methods=['POST'])
def home():
    data1 = request.form['a']
    data2 = request.form['b']
    data3 = request.form['c']
    data4 = request.form['d']
    data5 = request.form['e']
    data6 = request.form['f']
    data7 = request.form['g']
    data8 = request.form['h']
    data9 = request.form['i']
    data10 = request.form['j']
    data11= request.form['k']
    data12= request.form['l']
    arr = np.array([[data1, data2, data3,data4,data5,data6,data7,data8,data9,data10,data11,data12]])
    pred = model.predict(arr)
    return render_template('after.html',data=pred)


if __name__ == "__main__":
    app.run(debug=True)
