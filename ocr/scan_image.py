import cv2
import numpy as np
from keras.models import load_model
import pickle

model = load_model('sinhala_model_final.h5')
LB = pickle.load(open('label_binarizer.pkl', 'rb'))


def scan_image(img):
    img = cv2.resize(img, (80, 80))
    img_array = np.expand_dims(img, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    predicted_label = LB.inverse_transform(prediction)
    return predicted_label
