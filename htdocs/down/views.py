from django.shortcuts import render, redirect, reverse
from subprocess import run,PIPE
import sys  
import os
from pytube import YouTube
from django.contrib.sites.models import Site
from django.conf import settings
from wsgiref.util import FileWrapper
import mimetypes
from django.http import HttpResponse, FileResponse
from django.utils.encoding import smart_str
# from  django.core.files.base import file
import requests 
import os.path
from django.contrib import messages 
import youtube_dl
import datetime
from datetime import timedelta

# Create your views here.
def index(request):
    #return render(request, 'index.html',{'thumbnail':'/static/images/save.jpg'})
    return render(request, 'index.html',{'thumbnail':None})

def home(request):
    index(request)
 
def twitter(request):
     return render(request, 'twitter.html')

def videoDownload2(request):
    url=request.POST.get('userUrl')
    out= run([sys.executable,'down//urlsubmitted.py',url],shell=False,stdout=PIPE)  
    downloadLinks=''       
    video=YouTube(url)
    request.session['url'] = url
    for stream in video.streams.filter(progressive=True):
        if not (stream.resolution is None) and (stream.includes_audio_track) and (stream.includes_video_track):             
            downloadLinks +=('<li><a href="{videoLink}" download type="video/mp4" target="_blank">Download {resolution}</a></li>'.format(videoLink=stream.url, resolution=stream.resolution.strip())) 
    return render(request,'index.html',{'videoTitle':out.stdout, 'downloadLinks':downloadLinks})
    
def videoDownload(request):
    url=request.POST.get('userUrl')
    downloadLinks=''  
    options = {
    #'format': 'bestaudio/best',  # choice of quality
    #'extractaudio': True,        # only keep the audio
    #'audioformat': "mp3",        # convert to mp3
    'outtmpl': '%(id)s%(ext)s',         # name the file the ID of the video
    'noplaylist': True,          # only download single song, not playlist
    'listformats': True,         # print a list of the formats to stdout and exit
    }
  
    ydl = youtube_dl.YoutubeDL({'outtmpl': '%(id)s%(ext)s','verbose':True})
    with ydl:
        result = ydl.extract_info(
            url,
            download=False # We just want to extract the info
        )

    if result is not None:
        if 'entries' in result:
            # Can be a playlist or a list of videos
            video = result['entries'][0]
        else:
            # Just a video
            video = result

        #for loop
        title=video['title']
        thumbnail=video['thumbnail']
        #ts = int(video['timestamp'])         
        #a = datetime.timedelta(seconds=65)
        #datetime.timedelta(0, 65)

        #totalTime=str(a)
        totalTime='Thumbnail'
        for format in video['formats']:
            # only mp4
            if (format['ext'] == 'mp4') and ('protocol' in format) and (format['protocol']=='https' or format['protocol']=='http'):
                if ('acodec' in format and 'vcodec' in format) and (format['acodec']=='none'):
                    #no audio
                    pass
                else:      
                    formatSplited= format['format'].split("-")
                    resolution=formatSplited[-1].strip()
                    if str(resolution)=='unknown':
                        resolution= formatSplited[0]   
                    downloadLinks +=('<a href="{videoLink}" target="_blank" accesskey="1" title={title} class="list-group-item list-group-item-action">{resolution}</a>'.format(videoLink=format['url'], resolution=resolution, title=title)) 

        return render(request,'index.html',{'videoTitle':title,'userUrl':url,'thumbnail':thumbnail,'totalTime':totalTime ,'downloadLinks':downloadLinks})

    return render(request,'index.html', {'videoTitle':"Error: Result was empty.",'userUrl':url})
  
def downloadss(request):
    video_itag=request.GET.get('id')
    url=request.session.get('url')
    if url is not None:
        video=YouTube(url)
        # tempPath=os.getcwd() 
        outputFile = video.streams.get_by_itag(video_itag).download() 
                 
        root_Url=request.get_host()
    return redirect(reverse('http://%s/%s' % (root_Url, outputFile)))


def download(request):
    homedir = os.path.expanduser("~")
    dirs=homedir +'/Desktop'
    url=request.session.get('url')
    video_itag=request.GET.get('id')

    if request.method == "GET" and url is not None and video_itag is not None:   
        video=YouTube(url)
        video.streams.filter(progressive=True).get_by_itag(video_itag).download(homedir +'/Desktop')
        yyy=video.streams[0].url
        messages.success(request, 'video downloaded. Check your Download directory!')  

    #response = HttpResponse(YouTube(url).streams.filter(progressive=True).get_by_itag(video_itag).download(), content_type='video/mp4')
    #response['Content-Disposition'] = 'attachment; filename=my_video.mp4'
    #return response

    #yt = YouTube('http://youtube.com/watch?v=9bZkp7q19f0')
    #yt.streams.all()  # list of all available streams
    #yt.streams[0].url 

    return render(request, 'index.html')
   #response = FileResponse()
   #return response

