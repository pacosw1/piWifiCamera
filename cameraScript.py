import socketio
from config import startUp, setupStream, getFrame 
from time import sleep

client = startUp()
unique_id="AKLMNF14832"
camera_label="Kitchen"

@client.event
def connect():
        print('connection established')

@client.event
def disconnect():
    client.emit("disconnect", {"sid": client.sid, "_id": unique_id})

@client.on('connected')
def onIncomingData(data):
    print(data)
    print(client.sid)
    client.emit("connected", {"_id": unique_id, "sid": client.sid})


def runServer():
    
    fps = 10
    print("Starting camera")
    piCam = setupStream()
    sleep(2)

    while True:
        client.emit("feed", {"frame": getFrame(piCam), 'sid': client.sid, "_id": unique_id })
        sleep(1 / fps)
runServer()
