from django.urls import path, re_path
from .views import add, delete, index

urlpatterns = [
    path('', index),
    path('index', index),
    re_path(r'^delete/(?P<post_id>[0-9]+)$', delete),
    path('add', add),
]