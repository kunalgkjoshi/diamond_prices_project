# from tkinter import Y
from flask import Flask, request
import pickle
import pandas as pd

app = Flask(__name__)

with open(r'C:\Users\kunal\PycharmProjects\celebal_training\Practice_and_reports\Hands_on_ML_pracitce\model_pkl', 'rb') as f:
    model = pickle.load(f)

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':

        req_json = request.json

    prediction = model.predict(pd.DataFrame(req_json, index=[0]))

    return str(prediction)



if __name__ == '__main__':
    app.run(debug=True)

