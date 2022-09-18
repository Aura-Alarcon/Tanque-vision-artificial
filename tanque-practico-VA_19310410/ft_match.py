import cv2
import matplotlib.pyplot as plt

imagen1 = cv2.imread('aura1.png', 0)
imagen2 = cv2.imread('aura2.png', 0)

orb = cv2.ORB_create()
kp1, des1 = orb.detectAndCompute(imagen1, None)
kp2, des2 = orb.detectAndCompute(imagen2, None)
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
coin = bf.match(des1, des2)
coin = sorted(coin, key=lambda x: x.distance)
imagen3 = cv2.drawMatches(imagen1, kp1, imagen2, coin[:10], None, flags=2)
plt.imshow(imagen3)
plt.show()
