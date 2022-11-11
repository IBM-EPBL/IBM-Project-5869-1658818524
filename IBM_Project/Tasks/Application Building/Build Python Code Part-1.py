from flask import Flask,render_template,request
from PIL import Image
import numpy as np
from tensorflow.keras.models import load_model
import tensorflow as tf
app = Flask(__name__)
@app.route('/')
def upload_file():
    return render_template('home.html')

@app.route('/about')
def upload_file1():
    return render_template('home.html')

@app.route('/upload')
def upload_file2():
    return render_template('predict.html')

@app.route('/predict',methods = ['POST'])