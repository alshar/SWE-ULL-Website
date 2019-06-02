"""swesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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

urls.py defines the site url-to-view mappings. While this could contain all the url mapping code,
it is more common to delegate some of the mapping to particular applications.
"""


from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('pointstracker/', include('pointstracker.urls')),
    path('', include('base.urls')),
    path('about/', include('about.urls')),
    path('getinvolved/', include('getinvolved.urls')),
    path('events/', include('events.urls'))



]

"""
what include() does:
    anything after site.com/whatever will be "chopped off"
    and sent to whatever.urls to be processed. 
    Why do it this way? Abstraction. It's easier to do this 
    then have a massive url mapper in the main file 
"""

"""
path()'s arguments and what they do, found at the bottom of this page:
https://docs.djangoproject.com/en/2.2/intro/tutorial01/
"""