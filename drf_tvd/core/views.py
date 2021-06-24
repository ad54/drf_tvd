from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from .models import *
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.generics import ListAPIView, RetrieveAPIView, ListCreateAPIView, UpdateAPIView, DestroyAPIView, \
    CreateAPIView
from .serializers import *


class BooksAPI(ListAPIView, CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'id'


class BooksAPILookUp(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Book.objects.all()
    serializer_class = BookSerializers
    lookup_field = 'id'


class AuthorAPI(ListAPIView, CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    lookup_field = 'id'


class AuthorAPILookUp(RetrieveAPIView, DestroyAPIView, UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
    lookup_field = 'id'


class RegisterUser(APIView):
    """
    to register user and get access token
    """
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if not serializer.is_valid():
            return Response({'status': 403, 'error': serializer.errors, 'msg': 'data saved'})
        serializer.save()
        user = User.objects.get(username=serializer.data.get('username'))
        refresh = RefreshToken.for_user(user)

        return Response({'status': 200, 'payload': serializer.data, 'refresh': str(refresh),
                         'access': str(refresh.access_token), 'msg': 'user registered successfully'})
