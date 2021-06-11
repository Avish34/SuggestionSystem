from django.urls import path
from . import views
urlpatterns = [
   # path('webhook/', views.webhook, name='webhook'),
    path('get_suggestion', views.get_suggestion, name='get_suggestion')
]