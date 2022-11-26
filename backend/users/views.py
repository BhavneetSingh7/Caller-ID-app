from django.shortcuts import get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from rest_framework import generics, authentication, permissions
from rest_framework.decorators import api_view, APIView
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

class LoginView(APIView):
    queryset = get_user_model().objects.all()
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        pn = self.queryset.get(phone_number=request.POST['phone_number'])
        data = {
            'phone_number': request.POST.get('phone_number'),
            'name': pn.name,
            'password': request.POST.get('password'),
        }
        user = authentication.authenticate(request, phone_number=data['phone_number'])
        if user is not None:
            login(request, user)
            return redirect('users:profile')
        return redirect('users:login')

def Logout(request):
    return logout(request)