#!/usr/bin/python
import RPi.GPIO as GPIO
import picamera
import time
import os


#boardRevision = GPIO.RPI_REVISION
GPIO.setmode(GPIO.BCM) # use real GPIO numbering

#Setup LED Pins
lights = 4
GPIO.setup(lights, GPIO.OUT)

#Motion Sensor
motion_sensor = 12
GPIO.setup(motion_sensor, GPIO.IN)

#create instance of camera
camera = picamera.PiCamera()

#Start Numbering after last video
video = 0


# main loop

while True:

	try:

		if GPIO.input(motion_sensor) == True:

			GPIO.output(lights, True)

			while os.path.exists("video-%s.h264" % video):
				video += 1

			camera.start_recording("video-%s.h264" % video)
			time.sleep(60)
			camera.stop_recording()

			GPIO.output(lights, False)


	except KeyboardInterrupt:
	    GPIO.output(lights, False)
            camera.stop_recording()
	    camera.close()
            exit()
