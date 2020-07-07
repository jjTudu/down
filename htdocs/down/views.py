from django.shortcuts import render
from subprocess import run,PIPE
import sys  

# Create your views here.
def index(request):
    return render(request, 'index.html')

def home(request):
    index(request)


def videoDownload(request):
    url=request.POST.get('userUrl')
    out= run([sys.executable,'down//urlsubmitted.py',url],shell=False,stdout=PIPE) 
    #return render(request,'index.html',{'videoTitle':'hello james'})
    downloadLinks='''<li><a href="service-single.html">Pre-Construction</a></li>
				   <li><a href="service-single.html">General Contracting</a></li>
				   <li><a href="service-single.html">Construction Management</a></li>
				   <li><a href="service-single.html">Design and Build</a></li>
				   <li><a href="service-single.html">Self-Perform Construction</a></li>'''

    return render(request,'index.html',{'videoTitle':out.stdout, 'downloadLinks':downloadLinks})
    
