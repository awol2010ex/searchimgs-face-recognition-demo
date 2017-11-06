
import pickle

from scipy import misc
import numpy as np
import os


label = os.listdir("face")
dataset=[]
for image_label in label:

    images = os.listdir("face/"+image_label)

    for image in images:
        img = misc.imread("face/"+image_label+"/"+image)
        img = misc.imresize(img, (64, 64))
        if np.shape(img)==(64,64,3):
            dataset.append((img,image_label))



X=[]
Y=[]

for  input,image_label in dataset:

    X.append(input)

    Y.append(label.index(image_label))

X=np.array(X)
Y=np.array(Y)


X_train,y_train,  = X,Y


data_set=(X_train,y_train)


if not os.path.exists("./pickle"):
    os.mkdir("./pickle")
save_label = open("pickle/int_to_word_out.pickle","wb")
pickle.dump(label, save_label)
save_label.close()
