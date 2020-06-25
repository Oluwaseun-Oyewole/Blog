from django.urls import path
from . import views as user_views



urlpatterns = [
    # path('', user_views.home, name='home'),
    path('', user_views.HomePageView.as_view(), name='home'),
    path('post/<int:pk>/', user_views.DetailPageView.as_view(), name='detail'),
    path('post/new/', user_views.CreatePageView.as_view(), name='new'),
    path('post/<int:pk>/update/', user_views.UpdatePageView.as_view(), name='update'),
    path('post/<int:pk>/delete/', user_views.DeletePageView.as_view(), name='delete'),
    path('about/', user_views.about, name='about'),

]