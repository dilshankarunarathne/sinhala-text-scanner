import cv2
import numpy as np
from keras.models import load_model
import pickle

model = load_model('models/sinhala_model_final.h5')
LB = pickle.load(open('models/label_binarizer.pkl', 'rb'))


def scan_image(img):
    img = cv2.resize(img, (80, 80))
    img_array = np.expand_dims(img, axis=0)
    img_array = img_array / 255.0

    prediction = model.predict(img_array)

    predicted_label = LB.inverse_transform(prediction)
    return predicted_label


def sort_contours(cnts, method="left-to-right"):
    reverse = False
    i = 0
    if method == "right-to-left" or method == "bottom-to-top":
        reverse = True
    if method == "top-to-bottom" or method == "bottom-to-top":
        i = 1
    boundingBoxes = [cv2.boundingRect(c) for c in cnts]
    (cnts, boundingBoxes) = zip(*sorted(zip(cnts, boundingBoxes),
    key=lambda b:b[1][i], reverse=reverse))
    # return the list of sorted contours and bounding boxes
    return (cnts, boundingBoxes)


