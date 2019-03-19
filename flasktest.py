from flask import Flask, redirect, url_for, request
import cv2 as cv
import numpy as np
from PIL import Image
app = Flask(__name__)

@app.route('/sendImage',methods=["POST","GET"])
def getImage():
    data = request.data
    encoded_data = data.split(',')[1]
    nparr = np.fromstring(encoded_data.decode('base64'), np.uint8)
    img = cv.imdecode(nparr, cv.IMREAD_COLOR)
    cv.imshow(img)
    cv.waitKey(0)
    cv.destroyAllWindows()


if __name__ == '__main__':
   app.run(debug=True)