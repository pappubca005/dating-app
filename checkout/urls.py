# from django.conf.urls import url
from django.urls import re_path as url
from .views import subscribe

urlpatterns = [url(r"^$", subscribe, name="subscribe")]
