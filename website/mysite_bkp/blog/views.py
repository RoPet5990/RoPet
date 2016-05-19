from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .models import Post
from client import *
# Create your views here.

def post_list(request):
    while True:
        
        message = 'mmmmmmmmmmmmmmmm'
	print "======================"
        if request.GET.get('forward'):
            print "?????????????????"
	    message = "get button forward"
            motor_control('forward')
            
        if request.GET.get('backward'):
            message = "get button backward"
            motor_control('backward')
            
        if request.GET.get('stop'): 
            message = "get button stop"
            motor_control('stop')

	if request.GET.get('quit'): 
            message = "get button quit"
            motor_control('quit')
            
        if request.GET.get('resume'): 
            message = "get button resume"
            motor_control('resume')
            
        if request.GET.get('speed_up'): 
            message = "get button speed up"
            motor_control('up')
            
        if request.GET.get('speed_down'): 
            message = "get button speed down"
            motor_control('down')
            
        if request.GET.get('left'):
            message = "get button left"
            motor_control('left')
            
        if request.GET.get('right'): 
            message = "get button right"
            motor_control('right')

	if request.GET.get('watch'):
            url = request.get_host()
            ip_addr = url.split(":")[0]
            print "url is ==: %s" %(url)
            print 'ip_addr is == : %s' %(ip_addr)
        
        t = get_template('blog/post_list.html')
        html = t.render(Context({'message':message}))
        return HttpResponse(html)

