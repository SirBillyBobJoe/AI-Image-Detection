#this model is 70% accurate
import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from keras import datasets,layers,models

(training_images,training_labels), (testing_images, testing_labels)=datasets.cifar10.load_data()
training_images,testing_images=training_images/255,testing_images/255

class_names=['Plane','Car','Bird','Cat','Deer','Dog','Frog','Horse','Ship','Truck']
 


model=models.load_model('image_classifier.model')

img=cv.imread('images/cifar10images/horse.jpg')
img=cv.cvtColor(img,cv.COLOR_BGR2RGB)
img = cv.resize(img, (32, 32)) 

plt.imshow(img,cmap=plt.cm.binary)

prediction=model.predict(np.array([img])/255)
index=np.argmax(prediction)

print(f'Prediction is {class_names[index]}')