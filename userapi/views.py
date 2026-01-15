from django.shortcuts import render

from userapi.models import *
from userapi.serializers import*
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
from rest_framework.authtoken.models import Token
from django.shortcuts import get_object_or_404

# Create your views here.

class userregisterView(APIView):

    permission_classes =[AllowAny]

    def post(self,request):

        user_serializer = Userregisterationserializer(data= request.data)

        if user_serializer.is_valid():

            user = user_serializer.save()

            return Response(user_serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(user_serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    

class UserLoginView(APIView):

    permission_classes =[IsAuthenticated]

    authentication_classes = [BasicAuthentication]

    def post(self,request):

        user = request.user

        token,create =Token.objects.get_or_create(user=user)

        return Response({"message":"login success","token":token.key},status=status.HTTP_200_OK)
    

class SupportTicketAddListView(APIView):

    authentication_classes = [TokenAuthentication]

    permission_classes =[IsAuthenticated]

    def post(self,request):

        serializer = SupportTicketSerializer(data = request.data)

        if serializer.is_valid():

            serializer.save(user= request.user)

            return Response(serializer.data,status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
   