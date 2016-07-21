# Animated plot example using phao.mqtt.client library
# 
# This script will make a plot of temperature data recieved
# in json format. The x-axis is numbered 0-11. The y-data
# is fed into a ring-buffer and plotted as it is recieved
# from the mqtt.client.on_message call. Just about as simple 
# as it gets.
#

import matplotlib.pyplot as plt
import numpy as np
import paho.mqtt.client as mqtt
import json

temperature_data = np.linspace(0,0,11)
time_data = np.linspace(0,10,11)

plt.ion()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
line1, = ax1.plot(time_data, temperature_data, '-r')

plt.xlabel('time (not really)')
plt.ylabel('temperature')
plt.title('Last 10x Temperature Values')
plt.grid(True)

# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("debug")

# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    global temperature_data
    global time_data
    #print(msg.topic+" "+str(msg.payload))

    print(str(msg.payload, 'utf-8'))
    json_data = json.loads(str(msg.payload, 'utf-8'))
    temperature_data = np.roll(temperature_data, -1)
    temperature_data[-1] = float(json_data['temperature'])
    print("temperature_data: ")
    print(temperature_data)

    plt.ylim([temperature_data.min(), temperature_data.max()])

    #line1.set_xdata(time_data)
    line1.set_ydata(temperature_data)

    fig.canvas.draw()


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

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
