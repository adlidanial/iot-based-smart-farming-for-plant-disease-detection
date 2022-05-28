from os import getcwd
from flask import (render_template, Flask, request, redirect, url_for, session)
from flaskext.mysql import MySQL
from routes.connect import HOST, USER, PASSWORD, DB
from . import routes

import numpy as np
from keras.preprocessing import image
from keras.models import Model,Sequential, Input, load_model

app = Flask(__name__)

app.config['MYSQL_DATABASE_HOST'] = HOST
app.config['MYSQL_DATABASE_USER'] = USER
app.config['MYSQL_DATABASE_PASSWORD'] = PASSWORD
app.config['MYSQL_DATABASE_DB'] = DB

mysql = MySQL(app)

class Result:
    @routes.route('/result', methods = ['GET', 'POST'])
    def result():
        # model = tf.tflite.Interpreter(model_path='./models/PlantDiseaseModel.tflite')

        model = load_model('./models/PlantDiseaseModel.h5')
        img = image.load_img('./static/uploads/' + session["urlimage"], grayscale=False, target_size=(64, 64))
        # show_img=image.load_img(session["urlimage"], grayscale=False, target_size=(200, 200))
        disease_class = ['Chili_Healthy','Chili_Leaf_Curl','Chili_Leaf_Spot','Chili_Whitefly','Chili_Yellowish','Paddy_Brown_Spot','Paddy_Healthy','Paddy_Hispa','Paddy_Leaf_Blast']
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis = 0)
        #x = np.array(x, 'float32')
        x /= 255

        custom = model.predict(x)
        a=custom[0]
        ind=np.argmax(a)
        # print('Prediction:',disease_class[ind])

        cursor = mysql.get_db().cursor()
        cursor.execute('SELECT PK_ID, CONCAT(PLANT_NAME, "_", REPLACE(PLANT_DISEASE, " ", "_")) AS PLANTDISEASE FROM PLANTDISEASE')
        data = cursor.fetchall()
        
        for i in range(0, len(data)):
            if data[i][1] != str.upper(disease_class[ind]):
                continue
            else:
                cursor = mysql.get_db().cursor()
                cursor.execute('UPDATE LOGHISTORY SET FK_ID_DISEASE = %s WHERE PK_ID = %s', (data[i][0], session["lastid_loghistory"]))
                cursor.connection.commit()
                break

        return render_template('result.html', prediction = disease_class[ind], imgsrc ='/uploads/' + session["urlimage"])
