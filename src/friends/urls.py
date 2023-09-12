from django.contrib import admin
from django.urls import path, include
from .views import SuggestedFriendsView

urlpatterns = [
    path('<int:user_id>/',SuggestedFriendsView.as_view(), name='suggested-friends'),
   
]