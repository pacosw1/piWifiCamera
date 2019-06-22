from time import sleep
from picamera import PiCamera

camera = PiCamera()
print("Starting up")
sleep(2)
camera.capture("p.jpg")
