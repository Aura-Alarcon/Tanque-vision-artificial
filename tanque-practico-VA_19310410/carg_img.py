# Programa que se encarga de cargar la imagen y convertirla a escala de grises.

import cv2

img = cv2.imread('aura1.png', cv2.IMREAD_GRAYSCALE)
cv2.imshow('imagen', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
