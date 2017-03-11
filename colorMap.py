import numpy as np
import cv2
from matplotlib import pyplot as plt

#im_gray = cv2.imread('imgR.png', cv2.IMREAD_GRAYSCALE)
#im_color = cv2.applyColorMap(im_gray, cv2.COLORMAP_JET)

img = cv2.imread('imgR.png',0)

cv2.imshow = ("Test", img)
cv2.destroyAllWindows()


