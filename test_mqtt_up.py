import paho.mqtt.publish as publish
import time
import json

current_temp = 20

while current_temp < 30:
  d = {
      'sensor': '1',
      'temperature': str(current_temp),
  }
  json_msg = json.dumps(d)
  publish.single("debug", json_msg, hostname="cloud.stevelammers.com")
  time.sleep(1)
  current_temp = current_temp + 1

#print("Sending 0...")
#publish.single("debug", "Hello0", hostname="cloud.stevelammers.com")
#time.sleep(1)
#print("Sending 1...")
#publish.single("debug", "Hello1", hostname="cloud.stevelammers.com")
