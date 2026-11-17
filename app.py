import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sklearn
import pickle
import flask
from sklearn.linear_model import LinearRegression
from flask import Flask,render_template,request
with open("SLR_MODEL (1).pkl","rb") as b:
    model=pickle.load(b)


app=Flask(__name__)
@app.route("/")
def default_site():
    return render_template("index.html")

@app.route("/predict",methods=['GET','POST'])
def prediction():
    value=float(request.form['height'])
    value=np.array(value)
    result=model.predict([[value]])[0]
    return render_template("index.html",prediction=result)
if __name__=="__main__":
    app.run(debug=True)


