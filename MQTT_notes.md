## Mosquitto

mosquitto_sub -h cloud.stevelammers.com -i testSub -t debug

mosquitto_pub -h cloud.stevelammers.com -i testPublish -t debug -m "Hello World"

## Python
conda create --name IOT python=3 matplotlib
pip install phao-mqtt

## Problems
If plot does not show up (particularly in Ubuntu), you need to change the default backend variable in matplotlibrc file. Changing to TkAgg seems to work for Ubuntu 14.04. [instructions](http://stackoverflow.com/questions/7534453/matplotlib-does-not-show-my-drawings-although-i-call-pyplot-show)
