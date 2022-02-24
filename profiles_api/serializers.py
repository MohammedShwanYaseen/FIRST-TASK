from rest_framework import serializers
from task_2 import models


class UserProfileSerializer(serializers.ModelSerializer):
    """Serializes a user profile object"""
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name','password')
        extra_kwargs = {
            'password': {
                'write_only': True,
                'style': {'input_type': 'password'}
            }
        }

    def create(self, validated_data):
        """Create and return a new user"""
        user = models.UserProfile.objects.create_user(
            email=validated_data['email'],
            name=validated_data['name'],
            password=validated_data['password']
        )

        return user
class CategorySerializer(serializers.ModelSerializer):
    """Serializes categories"""
    class Meta:
        model = models.Category
        fields = ('id', 'name',)

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Course
        fields = ('id', 'name', 'description', 'overview', 'price',
         'created_at', 'updated_at', 'language', 'instructor', 'category')
        extra_kwargs = {'instructor': {'read_only': True}}

class ArticleSerializer(serializers.ModelSerializer):
    """Serializes articles"""
    class Meta:
        model = models.Article
        fields = ('name','text')
        extra_kwargs = {'author': {'read_only': True}}


class PartnerSerializer(serializers.ModelSerializer):
    """Serializes partners"""
    class Meta:
        model = models.Partner
        fields = ('name', 'logo',)
