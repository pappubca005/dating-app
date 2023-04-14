# from django.conf.urls import url
from django.urls import re_path as url
from .views import index, preregister

urlpatterns = [
    url(r"^$", preregister, name="preregister"),
    url(r"^home/", index, name="index"),
]
