from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Context
from .models import Post
from client import *
# Create your views here.

def post_list(request):
    print "?????"
	#posts = Post.objects.filter(title__contains='Django').order_by('title')
    while True:
        
        message = ''
        if 'cmd' in request.GET and request.GET['cmd']:
            cmd = request.GET['cmd']
            
            
            if cmd == 'forward':
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

            if cmd == 'watch':
                url = request.get_host()
                ip_addr = url.split(":")[0]
                print "url is ==: %s" %(url)
                print 'ip_addr is == : %s' %(ip_addr)
        
        t = get_template('blog/post_list.html')
        html = t.render(Context({'message':message}))
        print "%s" %(url)
        return HttpResponse(html)
    
def post_css(request):
    t_css = get_template('blog/post_css.css')
    css = t_css.render()
    return HttpResponse(css)
