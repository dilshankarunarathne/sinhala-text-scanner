import cv2
import imutils
import numpy as np
from keras.models import load_model
import pickle

model = load_model('models/sinhala_model_final.h5')
LB = pickle.load(open('models/label_binarizer.pkl', 'rb'))


def scan_image(img):
    # img = cv2.resize(img, (80, 80))
    # img_array = np.expand_dims(img, axis=0)
    # img_array = img_array / 255.0

    img_array = img  # use the passed image array directly

    prediction = get_letters(img_array)

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
    return (cnts, boundingBoxes)


def get_letters(image):
    letters = []

    # gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret,thresh1 = cv2.threshold(image ,127,255,cv2.THRESH_BINARY)
    dilated = cv2.dilate(thresh1, None, iterations=2)

    cnts = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)
    cnts = sort_contours(cnts, method="left-to-right")[0]
    # loop over the contours
    for c in cnts:
        if cv2.contourArea(c) > 10:
            (x, y, w, h) = cv2.boundingRect(c)
            x-=5
            y-=5
            w+=10
            h+=10
            # cv2.rectangle(image, (x, y), (x + w, y + h), (255, 255, 255), 2)
        roi = image[y:y + h, x:x + w]
        thresh = cv2.threshold(image, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
        thresh = cv2.resize(thresh, (80, 80), interpolation = cv2.INTER_CUBIC)
        thresh = thresh.astype("float32") / 255.0
        thresh = np.expand_dims(thresh, axis=-1)
        thresh = thresh.reshape(1,80,80,1)
        ypred = model.predict(thresh)
        ypred = LB.inverse_transform(ypred)
        [x] = ypred
        letters.append(x)
    return letters, image
