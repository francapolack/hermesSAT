import cv2
import numpy as np
import requests

url = "http://192.168.5.130/cam.jpeg"
resp = requests.get(url, stream=True).raw
image = np.asarray(bytearray(resp.read()), dtype="uint8")
image = cv2.imdecode(image, cv2.IMREAD_COLOR)

# for testing
cv2.imshow('esp32cam',image)
cv2.waitKey(0)
cv2.destroyAllWindows()
