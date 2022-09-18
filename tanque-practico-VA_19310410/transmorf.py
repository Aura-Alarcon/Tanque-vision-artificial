import cv2
import numpy as np

captura = cv2.VideoCapture(0)
while(1):
    _, frame = captura.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    r_ing = np.array([30, 150, 50])
    r_sup = np.array([255, 255, 180])

    mascara = cv2.inRange(hsv, r_ing, r_sup)
    res = cv2.bitwise_and(frame, frame, mask=mascara)
    cv2.imshow('Original', frame)
    cv2.imshow('Mask', mascara)
    kernel = np.ones((5, 5), np.uint8)

    ero = cv2.erode(mascara, kernel, iterations=1)
    cv2.imshow('Erosion', ero)
    dil = cv2.dilate(mascara, kernel, iterations=1)
    cv2.imshow('Dilatacion', dil)

    opening = cv2.morphologyEx(mascara, cv2.MORPH_OPEN, kernel)
    cv2.imshow('Opening', opening)

    closing = cv2.morphologyEx(mascara, cv2.MORPH_CLOSE, kernel)
    cv2.imshow('Closing', closing)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        break
cv2.destroyAllWindows()
captura.release()
