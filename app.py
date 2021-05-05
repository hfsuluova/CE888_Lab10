#This is Heroku Deployment Lectre
from flask import Flask, request, render_template
import os
import pickle

print(os.getcwd())
path = os.getcwd()

with open('Model/Pickle_RFC2.pkl', 'rb') as f:
    randomforest = pickle.load(f)


def get_predictions(age, sex, trestbps, chol, req_model):
    mylist = [age, sex, trestbps, chol]
    mylist = [float(i) for i in mylist]
    vals = [mylist]


    if req_model == 'RandomForest':
        #print(req_model)
        return randomforest.predict(vals)[0]

    else:
        return "Cannot Predict"


app = Flask(__name__)


@app.route('/')
def homepage():
    return render_template('home.html')


@app.route('/', methods=['POST', 'GET'])
def my_form_post():
    if request.method == 'POST':
        age = request.form['age']
        sex = request.form['sex']
        chol = request.form['chol']
        trestbps = request.form['trestbps']
        req_model = request.form['req_model']

        target = get_predictions(age, sex, trestbps, chol, req_model)

        if target==1:
            sale_making = 'Patient is likely to have the disease'
        else:
            sale_making = 'Patient is unlikely to have the disease'

        return render_template('home.html', target = target, sale_making = sale_making)
    else:
        return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)
