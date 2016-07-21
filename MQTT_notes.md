## Mosquitto

mosquitto_sub -h cloud.stevelammers.com -i testSub -t debug

mosquitto_pub -h cloud.stevelammers.com -i testPublish -t debug -m "Hello World"

## Python
conda create --name IOT python=3 matplotlib
pip install phao-mqtt
