# Programa que se encarga de cargar un video y convertirlo a escala de grises

import cv2

captura = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Formato para descomprimir
salida = cv2.VideoWriter('video1.mp4', fourcc, 20.0, (640, 480))

while(True):
    ret, frame = captura.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    salida.write(frame)
    cv2.imshow('frame', gray)
    if cv2.waitKey(1) & 0xFF == ord('c'):
        break

captura.release()
salida.release()
cv2.destroyAllWindows()
