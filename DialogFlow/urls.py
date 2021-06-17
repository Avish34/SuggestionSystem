from django.urls import path
from .controller import get_suggestion 
urlpatterns = [
   # path('webhook/', views.webhook, name='webhook'),
    path('get_suggestion',get_suggestion, name='get_suggestion')
]