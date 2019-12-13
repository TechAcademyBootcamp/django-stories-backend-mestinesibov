"""mysite URL Configuration

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
from django.urls import path
from polls.views import home_function
from polls.views import about_function
from polls.views import contact_function
from polls.views import create_story_function
from polls.views import single_function
from polls.views import stories_function
from polls.views import userp_function
from polls.views import email_function
from polls.views import recipes_function

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', home_function, name='homepage'),
    path('about/', about_function, name='aboutpage'),
    path('contact/', contact_function, name='contactpage'),
    path('create_story/', create_story_function, name='create_stpage'),
    path('single/', single_function, name='singlepage'),
    path('stories/', stories_function, name='stpage'),
    path('userp/', userp_function, name='userppage'),
    path('email/', email_function, name='emailpage'),
    path('recipes/', recipes_function, name='rpage'),

]
