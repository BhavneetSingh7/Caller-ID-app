from django.shortcuts import get_object_or_404
from rest_framework import generics, authentication, permissions
from users.serializers import (
    GlobalDBSerailizer, PersonalContactSerailizer,
    SpamDBSerailizer, UserSerializer
)
# from core.serializers import UserSerializer

class UserCreateView(generics.CreateAPIView):
    serializer_class = UserSerializer

class ManageUserView(generics.RetrieveUpdateDestroyAPIView):
    """Manage the authenticated user"""
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        """Retrieve and return the authenticated user"""
        return self.request.user