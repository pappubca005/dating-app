from django.conf.urls import include
from django.urls import re_path as url
from search.views import search

urlpatterns = [
    url(r"^$", search, name="search"),
]
