from django.urls import path
from .views import hello, fun, add_like

urlpatterns = [
    path('', hello),
    path('hello/', fun),
    path('add_like/', add_like),
]