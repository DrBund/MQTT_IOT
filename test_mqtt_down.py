import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.client as mqtt
import time
import json

temperature_data = []
time_data = []

plt.xlabel('time')
plt.ylabel('temperature')
plt.title('About as simple as it gets, folks')
plt.grid(True)
#plt.savefig("test.png")

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("debug")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    #print(msg.topic+" "+str(msg.payload))
    print(str(msg.payload, 'utf-8'))
    json_data = json.loads(str(msg.payload, 'utf-8'))
    temperature_data.append(float(json_data['temperature']))
    #temperature_data.append(10.0)
    time_data.append(time.time())
    #t = np.arange(0.0, 2.0, 0.01)
    #s = np.sin(2*np.pi*t)
    plt.plot(time_data, temperature_data)
    plt.show()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

#client.connect("iot.eclipse.org", 1883, 60)
client.connect("cloud.stevelammers.com", 1883, 60)

# Blocking call that processes network traffic, dispatches callbacks and
# handles reconnecting.
# Other loop*() functions are available that give a threaded interface and a
# manual interface.
client.loop_forever()










#print("Sending 0...")
#publish.single("debug", "Hello0", hostname="cloud.stevelammers.com")
#time.sleep(1)
#print("Sending 1...")
#publish.single("debug", "Hello1", hostname="cloud.stevelammers.com")
