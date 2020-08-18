
# Imports
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from UserDetails.api.serializers import UserSignUpSerializer, UserDetailsSerializer
from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from django.http import QueryDict

class UserRegister(APIView):
    """
    Creates the User
    """

    def post(self, request, format = 'json'):
        data = {}
        userSerializer = UserSignUpSerializer(data = request.data)
        if not userSerializer.is_valid():
            return Response(userSerializer.errors, status=status.HTTP_400_BAD_REQUEST)
        data["user"] = userSerializer.data
        data["user"]["password"] = request.data["password"]
        data["college"] = request.data.get("college")
        serializer = UserDetailsSerializer(data = data)
        if serializer.is_valid():
            user = serializer.save()
            token = Token.objects.create(user = user.user)
            json = serializer.data
            json['token'] = token.key
            return Response(json, status = status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request):
        return Response('Hello')