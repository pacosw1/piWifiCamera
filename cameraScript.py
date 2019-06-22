import socketio
from config import startUp
import time

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
    print("Loading feed")
    time.sleep(1.5)
    while True:
        client.emit("feed", {"data": "feed", 'sid': client.sid, "_id": unique_id })

runServer()
