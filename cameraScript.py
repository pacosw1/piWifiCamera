import socketio
import time

client = socketio.Client()

connection_refused = True
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

while connection_refused:
    try:
        client.connect('http://ec2-18-224-16-97.us-east-2.compute.amazonaws.com:4000/')
        
        connection_refused = False
    except:
        print("Connection failed. Retrying in 5s...")
        time.sleep(5)

while not(connection_refused):
    client.emit("feed", {"data": "feed", 'sid': client.sid, "_id": unique_id })

