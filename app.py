from turtle import title
from flask import Flask,request,render_template,session
import pandas as pd
import pre_processing
import model
import ner_model

app = Flask(__name__)

@app.route("/page", methods=['POST', 'GET'])
def page():
    df = pd.read_csv('ner.csv')
    return render_template("admin/forms.html",tables=[df.to_html(classes='table table-striped')], titles=df.columns.values)

@app.route("/ingredients", methods=['POST', 'GET'])
def preprocess():
    url = request.form['url']
    data = pre_processing.func(url)
    test = model.func2(data)
    ingredient = ner_model.ner_label(test)
    return ingredient

if __name__ == '__main__':
    app.run()