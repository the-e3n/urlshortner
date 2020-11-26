from django.urls import path
from . import views


urlpatterns = [
    path('<_url>',views.index),
    path('',views.index),
]
