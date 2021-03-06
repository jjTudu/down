"""htdocs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path 
from down.views import index, videoDownload, download, home, twitter
from django.conf import settings
from django.conf.urls.static import static

app_name = "down"

urlpatterns = [
    path('grappelli/', include('grappelli.urls')),
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('videoDownload/', videoDownload),
    path('home/', home),
    path('videoDownload/download/', download),
    path('twitter/', twitter, name='twitter'),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
