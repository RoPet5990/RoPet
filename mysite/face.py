from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2

def find_face():
    # Setup the camera
    found = False
    camera = PiCamera()
    camera.resolution = ( 320, 240 )
    camera.framerate = 60
    rawCapture = PiRGBArray( camera, size=( 320, 240 ) )

    # Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier( 'face.xml' ) 

    t_start = time.time()
    fps = 0
    t_end = t_start

    # Capture frames from the camera
    for frame in camera.capture_continuous( rawCapture, format="bgr", use_video_port=True ):
        
        image = frame.array
        
        # Use the cascade file we loaded to detect faces
        gray = cv2.cvtColor( image, cv2.COLOR_BGR2GRAY )
        faces = face_cascade.detectMultiScale( gray )

        # Clear the stream in preparation for the next frame
        rawCapture.truncate( 0 )

        print "Found " + str( len( faces ) ) + " face(s)"
        t_end = time.time()

        if t_end - t_start < 12 and len(faces) >= 1:
            found = True
            break
        elif t_end - t_start >= 12:
            break

    return found
