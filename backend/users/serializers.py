from rest_framework import serializers
from django.contrib.auth import get_user_model
from users.models import GlobalDB, SpamDB, PersonalContact


class GlobalDBSerailizer(serializers.ModelSerializer):
    """
    Serializer for Global DB API
    """
    class Meta:
        model = GlobalDB
        fields = [
            'id', 'country_code', 'phone_number', 'name',
            'is_personal_contact', 'created_at',
            ]


class PersonalContactSerailizer(serializers.ModelSerializer):
    """
    Serializer for Personal Contact DB API
    """
    class Meta:
        model = PersonalContact
        fields = [
            'id', 'phone_number', 'country_code', 'contact_of', 'created_at'
        ]


class SpamDBSerailizer(serializers.ModelSerializer):
    """
    Serializer for Spam DB API
    """
    class Meta:
        model = SpamDB
        fields = [
            'id', 'phone_number', 'country_code', 'marked_at'
        ]

def phone_number_format(num):
    """Splits country code and phone number"""
    return tuple(num.split('-'))

class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating user
    User is created for user model and global DB
    API is exposed for adding non registered user in global DB
    but only registered users can add global users
    """

    class Meta:
        model = get_user_model()
        fields = [
            'id','name','phone_number', 'email','password', 'created_at'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
                }
        }

    def create(self, validated_data):
        p = phone_number_format(validated_data.get('phone_number'))
        pn, cc = p[1], p[0]
        name = validated_data.get('name')
        email = validated_data.get('email')
        contact_gb = GlobalDB(phone_number=pn,country_code=cc,name=name,email=email,is_registered=True)
        contact_gb.save()
        return get_user_model().objects.create_user(**validated_data)

    def update(self, instance, validated_data):
        password = validated_data.pop('password', None)

        p = phone_number_format(validated_data.get('phone_number'))
        pn, cc = p[1], p[0]
        contact_gb = GlobalDB.objects.filter(phone_number=pn,country_code=cc,is_registered=True).first()
        contact_gb.name = validated_data.get('name')
        contact_gb.email = validated_data.get('email')
        contact_gb.save()
        user = super().update(instance, validated_data)

        if password:
            user.set_password(password)
            user.save()

        return user
