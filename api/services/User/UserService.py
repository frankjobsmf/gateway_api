#request
import requests

#firebase
from firebase_admin import auth

#PyJWT
import jwt
from datetime import datetime, timedelta

#rest_framework
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions

#serializers
from .userSerializers import (
    RegisterSerializer,
    LoginSerializer,
    LoginSocialSerializer,
)

URL_USER_API = 'http://127.0.0.1:8001/user/'

class RegisterAPI(APIView):
    
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = RegisterSerializer(data=request.data)
        
        if serializer.is_valid():
            
            endpoint_user = 'register'
            
            user_dict = {
                'username': serializer.validated_data['username'],
                'email': serializer.validated_data['email'],
                'password': serializer.validated_data['password'],
            }
            
            resp_user = requests.post(URL_USER_API + endpoint_user, json={'user_dict': user_dict}).json()
            
            return Response({
                "message": resp_user['message'],
                "status_code": resp_user['status_code']
            })
        
        return Response({
            "status_code": status.HTTP_400_BAD_REQUEST
        })

class LoginAPI(APIView):
    
    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid():

            endpoint_user = 'login'
            
            user_dict = {
                'username': serializer.validated_data['username'],
                'password': serializer.validated_data['password']
            }

            resp_user = requests.post(URL_USER_API + endpoint_user, json={'user_dict': user_dict}).json()

            #desestructurar user de la peticion
            user = resp_user['user']

            dt = datetime.now() + timedelta(days=15) 
            token = jwt.encode({'user': user, 'exp': dt}, 'secret-note-app', algorithm='HS256')

            return Response({
                "token": token,
                "status_code": status.HTTP_200_OK
            })
        
        return Response({
            "status_code": status.HTTP_400_BAD_REQUEST
        })


class LoginSocialAPI(APIView):
    
    serializer_class = LoginSocialSerializer

    def post(self, request, *args, **kwargs):

        serializer = LoginSocialSerializer(data=request.data)

        if serializer.is_valid():

            id_token = serializer.validated_data['id_token']

            decoded_token = auth.verify_id_token( id_token )

            email = decoded_token['email']

            print( email )

            return None

        return None