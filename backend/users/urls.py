from django.urls import path
from users import views
from users.views import (
    UserCreateView, ManageUserView
)

app_name = 'users'
urlpatterns = [
    # User profile CRUD registration, login and logout views
    path('create/',UserCreateView.as_view(),name='create'),
    path('<int:pk>/',ManageUserView.as_view(),name='profile'),
    # path('login/',ManageUserView.as_view(),name='login'),
    # path('logout/',ManageUserView.as_view(),name='logout'),

    # Authenticated users import contacts and filter queries
    # path('/',ManageUserView.as_view(),name='logout'),
    # path('/',ManageUserView.as_view(),name='logout'),
    # path('/',ManageUserView.as_view(),name='logout'),
]