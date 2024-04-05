
from rest_framework import serializers
from department.models import CustomUser , project



#create serializers here      

class CustomUserSerializer(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()    
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
        model=project
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