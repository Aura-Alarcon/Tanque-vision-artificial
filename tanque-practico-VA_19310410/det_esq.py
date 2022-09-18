import numpy as np
import cv2

imagen = cv2.imread('aura1.png')
gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
gris = np.float32(gris)

es = cv2.goodFeaturesToTrack(gris, 100, 0.01, 10)
es = np.int0(es)
for es in es:
    x, y = es.ravel()
    cv2.circle(imagen, (x, y), 3, 255, -1)

cv2.imshow('es', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
