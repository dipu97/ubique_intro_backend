from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Card


class UpdateUserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "email", "username", "first_name", "last_name", "bio", "job_title","company","contact", "location","address", "profile_picture",
                  "facebook", "youtube", "instagram", "twitter"]


class UserRegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "password"]
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        username = validated_data["username"]
        email = validated_data["email"]
        last_name = validated_data["last_name"]
        first_name = validated_data["first_name"]
        password = validated_data["password"]

        user = get_user_model()
        new_user = user.objects.create(username=username,first_name=first_name, email=email, last_name=last_name)
        new_user.set_password(password)
        new_user.save()
        return new_user


class SimpleAuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "first_name", "last_name", "email", "profile_picture"]


class CardSerializer(serializers.ModelSerializer):
    author = SimpleAuthorSerializer(read_only=True)

    class Meta:
        model = Card
        fields = ['id', 'title', 'slug','author' ,'category', 'sub_category', 'content','price', 'featured_image', 'published_date',
                  'created_at', 'updated_at', 'is_draft']


class UserInfoSerializer(serializers.ModelSerializer):
    author_posts = serializers.SerializerMethodField()

    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email", "first_name", "last_name", "job_title", "bio","company","facebook","instagram","twitter","contact","location","address","is_staff", "profile_picture",
                  "author_posts"]

    def get_author_posts(self, user):
        cards = Card.objects.filter(author=user)[:9]
        serializer = CardSerializer(cards, many=True)
        return serializer.data