#rest_framework
from rest_framework import serializers

#register
class RegisterSerializer(serializers.Serializer):
    username = serializers.CharField()
    email = serializers.EmailField()
    password = serializers.CharField()
    
#login
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()


#login social
class LoginSocialSerializer(serializers.Serializer):
    id_token = serializers.CharField()



#refresh token
class RefreshTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField()