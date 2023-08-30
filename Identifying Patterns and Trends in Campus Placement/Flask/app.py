# -*- coding: utf-8 -*-
"""
Created on Fri Dec 23 20:39:53 2022

@author: HI
"""

from flask import Flask, render_template , request
import pickle
import joblib

app = Flask(__name__)
model = pickle.load(open(r"C:\Users\harip\Downloads\GP3-20230309T045250Z-001\GP3\training\placement.pkl", 'rb'))
#ct=joblib.load('placement')


@app.route('/')
def hello():
    return render_template("index.html")


@app.route('/y_predict', methods=["POST"])
def y_predict(): 
    x_test = [[(yo) for yo in request.form.values()]]
    prediction =model.predict(x_test)
    prediction = prediction[0]
    return render_template("secondpage.html", y=prediction)


if __name__ == '__main__':
    app.run(debug=True)
