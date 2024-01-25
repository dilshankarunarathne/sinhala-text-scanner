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




# Preprocess the image
img = cv2.resize(img, (80,80))
img_array = np.expand_dims(img, axis=0)
img_array = img_array / 255.0

# Make a prediction
prediction = model.predict(img_array)

# Get the class label
predicted_label = LB.inverse_transform(prediction)
