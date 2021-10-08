import cv2
import numpy as np
# Ingresa valores RGB en los corchetes
color = np.uint8([[[255,255,0]]]) 
hsv_color1 = cv2.cvtColor(color,cv2.COLOR_BGR2HSV)
# Imprime valores en HSV
print (hsv_color1)