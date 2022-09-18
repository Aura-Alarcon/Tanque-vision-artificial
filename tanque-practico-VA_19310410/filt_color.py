import cv2
import numpy as np

captura = cv2.VideoCapture(0)
while(1):
    _, frame = captura.read()
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    r_inf = np.array([30, 150, 100])
    r_sup = np.array([255, 255, 180])

    mascara = cv2.inRange(hsv, r_inf, r_sup)
    resultado = cv2.bitwise_and(frame, frame, mask=mascara)

    cv2.imshow('frame', frame)  
    cv2.imshow('mascara', mascara)
    cv2.imshow('resultado', resultado)

    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

cv2.destroyAllWindows()
captura.release()
