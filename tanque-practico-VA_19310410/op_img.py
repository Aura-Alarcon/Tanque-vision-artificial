import cv2

imagen = cv2.imread('aura1.png', cv2.IMREAD_COLOR)
imagen[10, 10] = [255, 255, 255]
pixel = imagen[10, 10]
print(pixel)
imagen[30:150, 200:300] = [0, 0, 0]
print(imagen.shape)
print(imagen.size)
print(imagen.dtype)
captura = imagen[350:450, 600:700]
imagen[350:450, 350:450] = captura

cv2.imshow('imagen', imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
