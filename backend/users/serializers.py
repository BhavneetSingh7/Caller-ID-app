from rest_framework import serializers
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
    Serializer for Global DB API
    """
    class Meta:
        model = PersonalContact
        fields = [
            'id', 'personal_contact', 'personal_contact_of', 'created_at'
        ]


class SpamDBSerailizer(serializers.ModelSerializer):
    """
    Serializer for Global DB API
    """
    class Meta:
        model = SpamDB
        fields = [
            'id', 'phone_number', 'spam_marks', 'marked_by'
        ]