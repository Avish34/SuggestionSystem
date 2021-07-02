from django.urls import path
from .controller import get_accuracy, get_suggestion,update_collection,get_accuracy_patient
urlpatterns = [
    path('get_suggestion',get_suggestion, name='get_suggestion'),
    path('get_accuracy',get_accuracy, name='get_accuracy'),
    path('update_collection',update_collection,name='update_collection'),
    path('get_accuracy/patient',get_accuracy_patient,name='get_accuracy_paitent')
]