import paho.mqtt.publish as publish
import time
print("Sending 0...")
publish.single("debug", "Hello0", hostname="cloud.stevelammers.com")
time.sleep(1)
print("Sending 1...")
publish.single("debug", "Hello1", hostname="cloud.stevelammers.com")

