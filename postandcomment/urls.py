from django.urls import path
from . import views as user_views



urlpatterns = [
    path('', user_views.home, name='home'),
    path('about/', user_views.about, name='about'),
]