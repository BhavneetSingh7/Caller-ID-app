from rest_framework import generics, authentication, permissions
from users.models import GlobalDB, PersonalContact, SpamDB
from users.serializers import (
    GlobalDBSerailizer,SpamDBSerailizer, UserSerializer
)

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

class AddPersonalContact(generics.CreateAPIView):
    """
    First the personal contact is added in global DB
    then relation is created with registered user
    """
    queryset = GlobalDB.objects.all()
    serializer_class = GlobalDBSerailizer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        pn = serializer.validated_data['phone_number']
        cc = serializer.validated_data['country_code']
        name = serializer.validated_data['name']
        serializer.save(phone_number=pn, country_code=cc, name=name, is_personal_contact=True)

        contact_of = GlobalDB.objects.get(id=self.request.user.id)
        pc = PersonalContact(phone_number=pn, country_code=cc, contact_of=contact_of)
        pc.save()

class MarkSpamView(generics.RetrieveUpdateAPIView):
    """
    Get mark spam in global DB if the number is marked as spam more than or
    equal to 10 times and then save meta data of it in Spam DB
    """
    queryset = SpamDB.objects.all()
    serializer_class = SpamDBSerailizer
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        spam_phone_number = GlobalDB.objects.get(id=serializer.validated_data['spam_phone_number'])
        marked_by = GlobalDB.objects.get(id=self.request.user.id)
        pc = SpamDB(spam_phone_number,marked_by)
        pc.save()
        n = SpamDB.objects.filter(spam_phone_number=spam_phone_number).count()
        if n >= 10:
            spam_phone_number.is_marked_as_spam = True