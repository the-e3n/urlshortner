from django.urls import path
from . import views


urlpatterns = [
    path('create/',views.create),
    path('go/<_url>',views.index),
    path('',views.index2),
    path('list/',views.list_short),
]
