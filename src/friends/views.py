from rest_framework import generics
from rest_framework.response import Response
from .utils import calculate_jaccard_recommendations
from .serializers import UserSerializer
from  chatapp.settings import BASE_DIR
from .permissions import PublicAccessPermission
import os
import json

class SuggestedFriendsView(generics.ListAPIView):
    serializer_class = UserSerializer
    permission_classes = [PublicAccessPermission]
    def get_queryset(self):
        user_id = self.kwargs['user_id']
        
        # Build the path to the user_data.json file in STATIC_ROOT
        json_file_path = os.path.join(BASE_DIR, 'templates/user_data.json')
        

        try:
            with open(json_file_path, 'r') as json_file:
                data = json.load(json_file)
                users_data = data.get("users", [])

        except Exception as e:
            return {"message": "JSON file is not present","Exception":e}        
        # Implement Jaccard Index recommendation logic here.

        
        recommended_friends = calculate_jaccard_recommendations(user_id, users_data)
        return recommended_friends