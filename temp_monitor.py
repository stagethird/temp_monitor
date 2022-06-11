"""This program monitors and logs temperature using a Raspberry Pi and
an Adafruit AHT20 temperature and humidity sensor"""
#! /usr/bin/python3

def readAHT20():
    """
    This function reads and returns data from the Adafruit AHT20 sensor.
    It takes no input, and returns a list containing three floats.
    """
    import board
    import adafruit_ahtx0

    sensor = adafruit_ahtx0.AHTx0(board.I2C())
    c = round(sensor.temperature, 2)
    f = round(c * 1.8 + 32, 2)
    h = round(sensor.relative_humidity, 2)
    sensorList = [c, f, h]
    return (sensorList)

def dataWriter(data):
    """
    This function writes the temp (in degrees C and F), the relative humidity,
    and a time stamp to a file named 'temp_monitor_log.csv'.
    It takes a list containing 3 numbers, and returns an int, which is the
    current hour.
    """
    import os
    import csv
    import datetime

    logPath = 'temp_monitor_log.csv'
    header = ['Degrees C', 'Degrees F', 'Humidity', 'Timestamp']
    # Grab a timestamp and convert it from a dateTime object to a string
    time = str(datetime.datetime.now())
    # Split the string to remove fractions of a second and append it to the 'data' list
    data.append(time.split('.')[0])
    fileExist = False

    if os.path.isfile(logPath):
        fileExist = True
    with open(logPath, 'a') as csvfile:
        writer = csv.writer(csvfile)
        if fileExist == False:
            writer.writerow(header)
        writer.writerow(data)
    return datetime.datetime.now().hour

def LED_Function(temp):
    """
    This function controls the function of the indicator LED.
    It takes a number, and returns nothing.
    """
    import RPi.GPIO as GPIO

    threshold = 80
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(12, GPIO.OUT)
    if temp >= threshold:
        GPIO.output(12, GPIO.HIGH)
    else:
        GPIO.output(12, GPIO.LOW)
    return

def emailSender(data):
    """
    This function sends an email via SMTP using parameters defined below.
    It takes a list of three numbers, and returns nothing.
    """
    import smtplib

    # Email variables
    serverAddress = "smtp.HOSTDOMAIN.com"
    loginName = "LOGIN"
    loginPassword = "PASSWORD"
    senderAddress = "SENDER@HOSTDOMAIN.com"
    recipientAddress = "RECIPIENT@DOMAIN.com"

    emailBody = """\
Daily climate report from steve-pi0.

The current temperature is:
{} Degrees C.
{} Degrees F.
The relative humidity is:
{}%"""

    # Send email here
    server = smtplib.SMTP_SSL(serverAddress, 465)
    server.login(loginName, loginPassword)
    server.sendmail(
        senderAddress,
        recipientAddress,
        emailBody.format(data[0], data[1], data[2]))
    server.quit()
    return

def main():
    import sys

    try:
        data = readAHT20()
        hour = dataWriter(data)
        LED_Function(data[1])
        # If it's 4:00 PM, send out a status email.
        if hour == 16:
            emailSender(data)
        sys.exit(0)

    except Exception as e:
        print("Exception: ", e)
        sys.exit(1)

main()
