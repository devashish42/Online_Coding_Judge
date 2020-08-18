
# Imports
from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

# Custom Apps Imports
from UserDetails.models import UserDetails


# Default User Model
User = get_user_model()

class UserSignUpSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
            required=True,
            max_length = 32,
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    username = serializers.CharField(
            validators=[UniqueValidator(queryset=User.objects.all())]
            )
    password = serializers.CharField(min_length=8, write_only = True)

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'],
             validated_data['password'])
        return user

    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UserDetailsSerializer(serializers.ModelSerializer):

    user = UserSignUpSerializer()

    def create(self, data):
        validated_data = data["user"]
        user = User.objects.create_user(
                    validated_data['username'],
                    validated_data['email'],
                    validated_data['password']
                )
        user.save()
        userDetails = UserDetails.objects.create(
            user = user,
            college = data['college']
        )
        return userDetails

    class Meta:
        model = UserDetails
        fields = ['user', 'college']