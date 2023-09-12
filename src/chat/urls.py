from django.urls import path
from . import views

urlpatterns = [
    path('start/', views.start_convo, name='start_chat'),
    path('<int:convo_id>/', views.get_conversation, name='get_chat'),
    path('', views.conversations, name='chat')
]
