
import socketio

client = socketio.Client()


try:
    client.connect('http://test:5000')
except:
    print("Server is offline")


