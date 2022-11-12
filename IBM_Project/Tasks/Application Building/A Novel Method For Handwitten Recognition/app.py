from flask import Flask, jsonify, render_template, request
from PIL import Image
import numpy as np
# from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import os
from PIL import Image
from flask import Flask, request, render_template, url_for
# from werkzeug.utils import secure_filename, redirect
from keras.models import load_model
from keras.preprocessing import image
# from flask import send_from_directory


app = Flask(__name__)
app.secret_key = "ibm_project"

model = load_model('mnistCNN.h5')

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/recognise')
def recognize():
    return render_template('recongise.html')

@app.route('/predict' , methods=['GET','POST'])
def predict():
    data = request.files
    if request.method == 'POST':
        img = Image.open(data['file'].stream).convert("L")
        img = img.resize((28,28))
        im2arr = np.array(img)
        im2arr = im2arr.reshape(1,28,28,1)
        y_pred = model.predict(im2arr)
        maxi = np.amax(y_pred)
        classes_x=np.argmax(y_pred,axis=1)
        # print(type(classes_x))
        return jsonify(str(classes_x))
        # for idx, x in np.ndenumerate(y_pred):
        #     if x == maxi:
        #         print(idx)
        #         return jsonify(idx)
        # print(list(y_pred).index(max(y_pred)))

        return render_template('recongise.html')



if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8000,debug=True)
