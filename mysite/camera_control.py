import socket
import time
import picamera
import cv2

from picamera.array import PiRGBArray
from picamera import PiCamera

class CameraControl:
  def __init__(self):
    self.camera = None
    self.server_socket = None
    self.connection = None 
    
  def record(self):
    self.camera = picamera.PiCamera()
    self.camera.resolution = (640, 480)
    self.camera.framerate = 24
    
    self.server_socket = socket.socket()    
    self.server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    self.server_socket.bind(('0.0.0.0', 8080))
    self.server_socket.listen(0)

    # Accept a single connection and make a file-like object out of it
    self.connection = self.server_socket.accept()[0].makefile('wb')
    self.camera.start_recording(self.connection, format='h264')

  def stop(self):
    self.camera.stop_recording()
    self.server_socket.close()
    self.camera.close()
    self.connection.close()  
    
  def open(self):
    self.camera = picamera.PiCamera()

  def close(self):
    self.camera.close()
    
  def find_face(self):
    # Setup the camera
    found = False
    self.camera = picamera.PiCamera()
    self.camera.resolution = ( 320, 240 )
    self.camera.framerate = 60
    rawCapture = PiRGBArray( self.camera, size=( 320, 240 ) )

    # Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier( 'face.xml' ) 

    t_start = time.time()
    fps = 0
    t_end = t_start

    # Capture frames from the camera
    for frame in self.camera.capture_continuous( rawCapture, format="bgr", use_video_port=True ):
        
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