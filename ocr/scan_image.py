import cv2
import numpy as np
from keras.models import load_model
import pickle

# Load the model
model = load_model('sinhala_model_final.h5')
# Load the LabelBinarizer
LB = pickle.load(open('label_binarizer.pkl', 'rb'))
# Load the image
img = cv2.imread('test.jpg',0)
