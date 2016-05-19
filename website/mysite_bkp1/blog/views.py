from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from django.template import loader
from .models import *
from client import *
from dogsearch import *
import subprocess
import psutil
# Create your views here.

PROCNAME = 'dogsearch.py'

def post_list(request):
    print "?????"
	#posts = Post.objects.filter(title__contains='Django').order_by('title')
    while True:
        
        message = ''
        
        if 'cmd' in request.GET and request.GET['cmd']:
            cmd = request.GET['cmd']
            
            if cmd == 'forward':
            	print "======in forward======"
                message = "get button forward"
                motor_control('forward')
		
            if cmd == 'backward': 
                message = "get button backward"
                motor_control('backward')

            if cmd == 'stop': 
                message = "get button stop"
                motor_control('stop')

            if cmd == 'quit': 
                message = "get button quit"
                motor_control('quit')

            if cmd == 'resume': 
                message = "get button resume"
                motor_control('resume')

            if cmd == 'speed_up': 
                message = "get button speed up"
                motor_control('up')

            if cmd == 'speed_down': 
                message = "get button speed down"
                motor_control('down')

            if cmd == 'left':
                message = "get button left"
                motor_control('left')

            if cmd == 'right': 
                message = "get button right"
                motor_control('right')

            if cmd == 'record':
                camera.record()

            if cmd == 'stop_record':
                camera.stop()

            if cmd == 'blt_on':
                print "dogsearch"
#                dogsearch()
                p = subprocess.Popen("sudo python dogsearch.py", shell=True)
                
            if cmd == 'blt_off':
                p.terminate()
            
        print "message is %s" %(message)
       	t = get_template('blog/post_list.html')
        html = t.render({'message':message})
       	return HttpResponse(html) 
