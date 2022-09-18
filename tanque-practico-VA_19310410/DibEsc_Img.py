# Creada y dibuja figuras sobre la misma imagen

import numpy as np
import cv2

imagen = cv2.imread('aura1.png', cv2.IMREAD_COLOR)
cv2.line(imagen, (100, 0), (0, 100), (255, 124, 32), 5)
cv2.rectangle(imagen, (423, 80), (70, 310), (43, 12, 255), 5)
cv2.circle(imagen, (20, 380), 50, (12, 255, 123), 5)
pts = np.array([[100, 50], [200, 300], [700, 200], [500, 100]], np.int32)
pts = pts.reshape((-1, 1, 2))
cv2.polylines(imagen, [pts], True, (0, 255, 255), 3)
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(imagen, 'Yo', (150, 650), font, 6, (0, 0, 0), 13, cv2.LINE_AA)
cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
