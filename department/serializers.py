
from typing import Generic
from rest_framework import serializers
from department.models import CustomUser , Project



#create serializers here      

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
    # this meta is used to coustamize which fields do we need from the models
    # It will automatically generate a set of fields for you, based on the model. 
    # It will automatically generate validators for the serializer, such as unique_together validators.
    class Meta:
        model=CustomUser
        fields="__all__"

class RegiterSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class meta:
        model= CustomUser
        fields="__all__"

class projectSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
    class Meta:
        model=Project
        fields="__all__"
class LoginSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField
    class Meta:
        model=CustomUser
        fields="__all__"
class ChangePasswordSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField
    class Meta:
        model=CustomUser
        fields="__all__"

class ResetPasswordEmailRequestSerializer(serializers.Serializer):
    email = serializers.EmailField(min_length=2)

    def validate_email(self, email):
        # Check if the email is already in the database
        try:
            CustomUser.objects.get(email=email)
        except CustomUser.DoesNotExist:
            raise serializers.ValidationError({"email": "Please enter a valid email address."})
        return email
    class Meta:
        fields  = ["email"]
