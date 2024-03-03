from django.urls import path
from .views import index, ajax_send_voicemail

urlpatterns = [
    path('', index, name='index'),  # For rendering the main page
    path('send_voicemail/', ajax_send_voicemail, name='send_voicemail'),
]