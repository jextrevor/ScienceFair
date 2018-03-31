#Import necessary libraries. picamera is used to control the camera, subprocess is used to provide the voice, GPIO is used to setup the camera, io is used to capture streams, PIL is used to analyse the images.
import picamera
import io
import subprocess
import RPi.GPIO as GPIO
from PIL import Image
#Set up necessary variables. Delta is the amount of change required in a pixel for it to be marked as changed, and threshold is the number of pixels that must be changed for the picture to count as changed.
#Occupied is the Boolean variable that keeps track of whether or not there is a person in the scene. camera, GPIO, and CAMLED are used to setup the camera.
delta = 35
threshold = 200
occupied = False
camera = picamera.PiCamera()
GPIO.setmode(GPIO.BCM)
CAMLED = 32
GPIO.setup(CAMLED, GPI0.0UT, initial=False)
#This function is used to take a picture (Resolution 50 pixels by 25 pixels) using the camera. It returns an array of the
pixels in the image.
def captureTestImage():
    camera.resolution = (50, 25)
    stream = io.BytesIO()
    camera.capture(stream, format='bmp')
    stream.seek(0)
    im = Image.open(stream)
    buffer = im.load()
    stream.close()
    return buffer
#A few pictures are taken to help settle the camera.
a = captureTestImage()
b = captureTestImage()
c = captureTestImage()
d = captureTestImage()
e = captureTestImage()
#A preliminary picture is taken to provide comparison.
buffer1 = captureTestImage()
#This function takes an input string and uses the espeak library to provide voice synthesization.
def say(string):
    p = subprocess.Popen('espeak "'+string+'"',stdout=subprocess.PIPE,shell=True)
    (output, err) = p.communicate()
    return output
say("ready for action")
#This thread continously takes pictures and compares them to the original picture.
def motionthread():
    global buffer1, occupied, delta, threshold
    while True:
        # Get comparison image.
        buffer2 = captureTestImage()
        
        # Count changed pixels.
        changedPixels = O
        for x in xrange(0, 50):
            for y in xrange(0, 25):
                # Check green channel as it’s the highest quality channel.
                pixdiff = abs(buffer1[x,y][1] - buffer2[x,y][1])
                if pixdiff > delta:
                    changedPixels += 1
        # Say hi if the threshold has been crossed.
        if changedPixels > threshold:
            if occupied == False:
                print "hi"
                occupied = True
                say("Hello")
        # Say bye if the threshold has been crossed the other way.
        if changedPixels <= threshold:
            if occupied == True:
                print "bye"
                occupied = False
                say("Goodbye")
            else:
                buffer1 = buffer2
motionthread()
