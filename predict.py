#!/usr/bin/env python
# -*- coding:utf-8 -*-
import numpy as np
import os
from scipy import  misc
import dlib
from skimage import io
from keras.models import model_from_json
import pickle
detector = dlib.get_frontal_face_detector()


classifier_f = open("pickle/int_to_word_out.pickle", "rb")
int_to_word_out = pickle.load(classifier_f)
classifier_f.close()



# load json and create model
json_file = open('model/model_face.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model/model_face.h5")
print("Model is now loaded in the disk")


imgs=os.listdir("predict")
print(int_to_word_out)
if len(imgs)>0 :
    for img  in imgs:
        #抓取头像
        image=[]
        try:
            imgF =misc.imread("predict/"+img)
            dects = detector(imgF, 1)
            for i, rect in enumerate(dects):
                image =  imgF[rect.top():rect.bottom(), rect.left():rect.right()]
                break;
        except Exception as err:
            time.sleep(1)
            print(err)
            print("读取图像错误")
            continue
        #image=np.array(misc.imread("predict/"+img))
        image = misc.imresize(image, (64, 64))
        
        
        image=np.array([image])
        image = image.astype('float32')
        image = image / 255.0

        prediction=loaded_model.predict(image)
        print(img +"-----------------")
        print(prediction)

        print(np.max(prediction))
         
        print(int_to_word_out[np.argmax(prediction)])
        print("-----------------")