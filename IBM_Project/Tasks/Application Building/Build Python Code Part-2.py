def upload_image_file():
    if request.method=='POST':
        img = Image.open(request.files['file'].stream).convert("L")
        img = img.resize((28,28))
        img2arr = np.array(img)
        img2arr = img2arr.reshape(1,28,28,1)
        model = load_model('models/model.h5')
        #y_pred = model.predict_classes(img2arr)
        y_pred = np.argmax(model.predict(img2arr), axis=1)
        print(y_pred)
        if(y_pred == 0):
            return render_template("0.html",shoechase = str(y_pred))
        elif(y_pred == 1):
            return render_template("1.html",shoechase = str(y_pred))
        elif(y_pred == 2):
            return render_template("2.html",shoechase = str(y_pred))
        elif(y_pred == 3):
            return render_template("3.html",shoechase = str(y_pred))
        elif(y_pred == 4):
            return render_template("4.html",shoechase = str(y_pred))
        elif(y_pred == 5):
            return render_template("5.html",shoechase = str(y_pred))
        elif(y_pred == 6):
            return render_template("6.html",shoechase = str(y_pred))
        elif(y_pred == 7):
            return render_template("7.html",shoechase = str(y_pred))
        elif(y_pred == 8):
            return render_template("8.html",shoechase = str(y_pred))
        else:
            return render_template("9.html",shoechase = str(y_pred))
    else:
        return None
    
if __name__=='__main__':
    app.run()
