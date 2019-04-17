from django.urls import path
from .views import hello, fun

urlpatterns = [
    path('', hello),
    path('hello/', fun),
]