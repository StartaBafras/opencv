def ele():
    import cv2
    import numpy as np
    resim = cv2.imread("Harf1.jpg")
    cv2.imshow("de",resim)
    kes = resim[0:140,0:370]
    cv2.imshow("d",kes)
    cv2.waitKey()
    cv2.destroyAllWindows()


import cv2
import pytesseract
from PIL import Image

img_cv = cv2.imread("Harf2.png")

# By default OpenCV stores images in BGR format and since pytesseract assumes RGB format,
# we need to convert from BGR to RGB format/mode:
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))
#Veya
img_rgb = Image.frombytes('RGB', img_cv.shape[:2], img_cv, 'raw', 'BGR', 0, 0)
print(pytesseract.image_to_string(img_rgb))
