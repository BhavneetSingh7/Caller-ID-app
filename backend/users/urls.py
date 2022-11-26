from django.urls import path
from users import views
from rest_framework.urls import urlpatterns
from users.views import (
    UserCreateView, ManageUserView,
    AddPersonalContact, MarkSpamView
)

app_name = 'users'
urlpatterns = [
    # User profile CRUD registration, login and logout views
    path('create/',UserCreateView.as_view(),name='create'),
    path('',ManageUserView.as_view(),name='profile'),

    # Authenticated users can import contacts in Global DB and mark spam
    path('add/',AddPersonalContact.as_view(),name='add'),
    path('spam/',MarkSpamView.as_view(),name='spam'),

    # filter views and search queries
]