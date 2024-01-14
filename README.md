# Temperature Monitor (temp_monitor.py)

This program runs on a Raspberry Pi, monitoring a temperature and humidity
sensor and recording the data collected.

-----
On starting up the program first reads an __Adafruit AHT20__ sensor and stores
the temperature and humidity values. It then grabs a timestamp and writes
the degrees C, degrees F, humidity, and timestamp to a .CSV file, creating
it if neccessary. After this it checks the temperature and activates an LED 
attached to the Pi's GPIO header if it exceeds 80F. The last thing it does is 
check the timestamp, and if the hour == 4:00 PM it sends an email summary using 
account details that are stored as constants in a seperate module.

-----
The program is designed to be run by the Raspberry Pi's `cron` task
scheduler, it runs once then exits without writing anything to `stdout`.

-----
I've uploaded a copy of of the log file, named `temp_monitor_log.csv`.

-----
I've uploaded a `Jupyter Notebook` as well, showing various ways that I've
plotted and analysed the data logged.  [![Colab](https://colab.research.google.com/assets/colab-badge.svg)]( https://colab.research.google.com/github/stagethird/temp_monitor/blob/master/temp_monitor.ipynb)
