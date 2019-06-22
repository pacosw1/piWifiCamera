import socketio
import time
import cv2
import base64
serverURL = "http://ec2-18-188-147-157.us-east-2.compute.amazonaws.com:4000"

client = socketio.Client()
def startUp():
    connection_refused = True
    while connection_refused:
        try:
            client.connect(serverURL)
            connection_refused = False
            return client
        except:
            print("Connection lost. Attempting to reconnect in 5s")
            time.sleep(5);

def setupStream():
    return cv2.VideoCapture(0)

def getFrame(piCam):
    okFrame, frame = piCam.read()
    if okFrame:
        okImage, image = cv2.imencode('.jpg', frame)
        if okImage:
            decoded = base64.b64encode(image)
    return decoded
