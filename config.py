import socketio
import time
serverURL = "http://ec2-18-224-16-97.us-east-2.compute.amazonaws.com:4000"

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
    
