from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from .models import Account
from .serializers import AccountSerializer

class UserRegister(APIView):
    serializer_class = AccountSerializer
    permission_class = (AllowAny,)

    def post(self, request, format=None):
        '''
        Register a new user
        '''
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class UserLogin(APIView):
    authentication_classes = (SessionAuthentication)
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        '''
        Login a user
        '''
        username = request.POST['username']
        print('Username', username)
        password = request.data['password']
        user = authenticate(request, username=username, password=password)
        print('User', user)
        if user is not None and user.is_active:
            # Correct password, and the user is marked "active"
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect("/account/loggedin/")
        else:
            # Show an error page
            return HttpResponse("User not logged in")


class Home(APIView):
    def get(self, request):
        print('You have logged in Succesfully')
