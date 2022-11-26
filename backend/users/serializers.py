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
            'is_registered', 'is_personal_contact', 'is_marked_as_spam',
            'created_at',
            ]


class PersonalContactSerailizer(serializers.ModelSerializer):
    """
    Serializer for Personal Contact DB API
    """
    class Meta:
        model = PersonalContact
        fields = [
            'id', 'personal_contact', 'contact_of', 'created_at'
        ]


class SpamDBSerailizer(serializers.ModelSerializer):
    """
    Serializer for Spam DB API
    """
    class Meta:
        model = SpamDB
        fields = [
            'id', 'spam_phone_number', 'marked_by', 'marked_at'
        ]


class UserSerializer(serializers.ModelSerializer):
    """
    Serializer for creating and updating user
    """

    class Meta:
        model = get_user_model()
        fields = [
            'id','name','phone_number', 'email', 'created_at'
        ]
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 5
                }
        }

    def create(self, validated_data):
        return super().create(validated_data)

    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
