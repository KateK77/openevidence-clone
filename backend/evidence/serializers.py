from django.contrib.auth.models import User
from rest_framework import serializers

from .models import Preferences
from .pubmed import TYPES


class Credentials(serializers.Serializer):
    username = serializers.CharField(max_length=150, validators=[User.username_validator])
    password = serializers.CharField(max_length=128, trim_whitespace=False, write_only=True)


class Question(serializers.Serializer):
    question = serializers.CharField(min_length=5, max_length=2000, trim_whitespace=True)
    conversation = serializers.IntegerField(min_value=1, required=False)


class Title(serializers.Serializer):
    title = serializers.CharField(max_length=180)


class Profile(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']
        read_only_fields = ['username']


class Settings(serializers.ModelSerializer):
    language = serializers.ChoiceField(choices=['English', 'Chinese', 'Spanish', 'French'])
    detail = serializers.ChoiceField(choices=['Concise', 'Standard', 'Detailed'])
    display = serializers.ChoiceField(choices=['Comfortable', 'Compact'])

    class Meta:
        model = Preferences
        fields = ['language', 'detail', 'display']


class LiteratureQuery(serializers.Serializer):
    q = serializers.CharField(max_length=400)
    year = serializers.IntegerField(min_value=1800, max_value=2100, required=False)
    journal = serializers.CharField(max_length=100, required=False)
    article_type = serializers.ChoiceField(choices=TYPES, required=False)
    free = serializers.BooleanField(required=False)
    sort = serializers.ChoiceField(choices=['relevance', 'pub date'], default='relevance')


class Collection(serializers.Serializer):
    collection = serializers.CharField(max_length=80, allow_blank=True, default='')
