import cv2
import numpy as np

captura = cv2.VideoCapture(0)
while(1):
    _, frame = captura.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    r_inf = np.array([30, 150, 50])
    r_sup = np.array([255, 255, 180])

    mascara = cv2.inRange(hsv, r_inf, r_sup)
    res = cv2.bitwise_and(frame, frame, mask=mascara)
    cv2.imshow('Original', frame)
# suavizado
    kernel = np.ones((15, 15), np.float32)/225
    suavizado = cv2.filter2D(res, -1, kernel)
    cv2.imshow('suavizado', suavizado)
# difuminado gausanio
    gauss = cv2.GaussianBlur(res, (15, 15), 0)
    cv2.imshow('difuminado gausanio', gauss)
# difuminado mediano
    med = cv2.medianBlur(res, 15)
    cv2.imshow('difuminado mediano', med)
# difuminado bilateral
    bil = cv2.bilateralFilter(res, 15, 75, 75)
    cv2.imshow('difuminado bilateral', bil)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cv2.destroyAllWindows()
captura.release()
