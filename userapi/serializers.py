from rest_framework import serializers

from userapi.models import *

class Userregisterationserializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields =['username','email','password']

    def create(self, validated_data):
        
        user = User.objects.create_user(
            username=validated_data['username'],
            password =validated_data['password'],
            email = validated_data['email']
        )
        return user
   



