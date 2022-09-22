# Temperature Monitor (temp_monitor.py)

This program runs on a Raspberry Pi, monitoring a temperature and humidity
sensor and recording the data collected.

-----
On starting up the program first reads an Adafruit AHT20 sensor and stores
the temperature and humidity values. It then grabs a timestamp and writes
the degrees C, degrees F, humidity, and timestamp to a .CSV file, creating
it if neccessary. After this it checks the temperature and activates an LED 
attached to the Pi's GPIO if it exceeds 80F. The last thing it does is 
check the timestamp, and if the hour = 4PM it sends an email summary using 
account details that are stored as constants in a seperate module.

-----
The program is designed to be run by the Raspberry Pi's `cron` task
scheduler, it runs once then exits without writing anything to `stdout`.
