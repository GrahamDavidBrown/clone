from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^city_pick/', views.home, name='home'),
]
