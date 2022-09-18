import cv2

imagen = cv2.imread('ejemplo1.jpg')
retval, th = cv2.threshold(imagen, 12, 255, cv2.THRESH_BINARY)
cv2.imshow('original', imagen)
cv2.imshow('th1', th)

escalagris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
retval2, th2 = cv2.threshold(escalagris, 10, 255, cv2.THRESH_BINARY)
cv2.imshow('th2', th2)
th = cv2.adaptiveThreshold(escalagris, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
cv2.imshow('Ath', th)

retval3, th3 = cv2.threshold(escalagris, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)
cv2.imshow('Oth', th3)
cv2.waitKey(0)
cv2.destroyAllWindows()
