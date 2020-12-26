from sensorhub.hub import SensorHub
from picamera import PiCamera
from time import time, ctime, sleep
from datetime import datetime 
from twilio.rest import Client

hub = SensorHub(None)
client = Client("USER ID", "Auth Token")
captureFile = 'FILE TO CAPTURE TO'

def sendAlert():
    client.messages.create(to="RECEIVE NUMBER", 
                       from_="FROM NUMBER", 
                       media_url=[captureFile],
                       body="-- MOTION SENSOR NOTIFICATION --\n   Motion Detection Triggered @ {}".format(ctime(t)))

# Detecting time to set exposure type needs work.

def recordMovement():
    camera = PiCamera()
    hour = todays_date.hour
    if hour >= 9 & hour < 22:
        exposure = "night"
        print("[-] Exposure set to night {}".format(ctime(t)))
    else:
        exposure = "off"
        print("[-] Exposure set to day {}".format(ctime(t)))
    camera.exposure_mode = exposure
    camera.resolution = (1920, 1080)
    camera.framerate = 30
    camera.annotate_text = "Motion Detected @ {}".format(ctime(t))
    camera.start_preview()
    camera.start_recording(captureFile)
    sleep(15)
    camera.stop_recording()
    camera.stop_preview()
    camera.close()

print("--------------------- \n        LOADED        \n---------------------")

while True:
    t = time()
    todays_date = datetime.now()
    successfulSend = "[!] A message was sent at {}".format(ctime(t))

    if hub.is_motion_detected() == True:
        recordMovement()
        sendAlert()
        print(successfulSend)


