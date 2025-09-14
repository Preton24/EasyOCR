import easyocr
import cv2
from matplotlib import pyplot as plt

IMAGE_PATH = 'DangerSign.jpg'

reader = easyocr.Reader(['en'])
results = reader.readtext(IMAGE_PATH)
img = cv2.imread(IMAGE_PATH)
font = cv2.FONT_HERSHEY_SIMPLEX

for detection in results:
    coords, text, confidence = detection
    top_left = tuple(map(int, coords[0]))
    bottom_right = tuple(map(int, coords[2]))
    img = cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2) 
    img = cv2.putText(img, text, (top_left[0], top_left[1] - 10), font, 
                      0.7, (255, 0, 0), 2, cv2.LINE_AA)

plt.figure(figsize=(10,10))
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()
