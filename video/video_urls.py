from django.urls import path
from .views import hello, fun, add_like, add_comment

urlpatterns = [
    path('', hello),
    path('hello/', fun),
    path('add_like/', add_like),
    path('add_comment/', add_comment),
]