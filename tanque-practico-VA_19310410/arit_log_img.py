import cv2
import numpy as np

imagen1 = cv2.imread('ejemplo1.jpg')
imagen2 = cv2.imread('ejemplo2.jpg')
add = cv2.add(imagen1, imagen2)
weighted = cv2.addWeighted(imagen1, 0.6, imagen2, 0.4, 0)

cv2.imshow('add', add)
cv2.imshow('weighted', weighted)
cv2.waitKey(0)
cv2.destroyAllWindows()
