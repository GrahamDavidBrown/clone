"""craigslist_clone URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
from clone import views
urlpatterns = [
    url(r'^$', auth_views.login),
    url(r'^admin/', admin.site.urls),
    url(r'^login/$', auth_views.login, name='login'),
    url(r'^clone/', include('clone.urls')),
    url(r'accounts/profile/', views.home,),
    url(r'^mylistings/', views.mylistings),
    # url(r'^city_listings/', views.city_listings),
    url(r'^city_listings/(?P<city_id>[\w\s]+)/', views.city_listings),
    url(r'^category_view/(?P<city_id>[\w\s]+)/(?P<sub_cat>[\w\s]+)/', views.category_view),
    url(r'^register/', views.register),
    url(r'^registration/', views.registration),
    url(r'^new_listing/(?P<city_id>[\w\s]+)/(?P<sub_cat>[\w\s]+)/', views.new_listing),
    url(r'^create_listing/(?P<city_id>[\w\s]+)/(?P<sub_cat>[\w\s]+)/', views.create_listing)
]
