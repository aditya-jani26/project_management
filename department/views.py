from rest_framework import viewsets 
from django.contrib.auth.models import User
from department.permission import CanCreateProjectPermission  # Update import path
from department.serializers import CustomUserSerializer, projectSerializer ,RegiterSerializer ,LoginSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.contrib.auth import authenticate

class RegisterView(APIView):    
    def post(self, request, format=None):
        serializer = RegiterSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            # No token generation here
            return Response({'Successful': 'Registration Successful..!'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class LoginView(APIView):
    def post(self, request, format=None):
        serializer = LoginSerializer(data=request.data)
        
        if serializer.is_valid(raise_exception=True):
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(email=email, password=password)
            if user is not None:
                return Response({"Successful": "Login Successful..!"}, status=status.HTTP_200_OK)
            else:
                return Response({"error": "Invalid Credentials..!"}, status=status.HTTP_401_UNAUTHORIZED)    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        

class CustomUserViewSet(viewsets.ModelViewSet):
    
    serializer_class = CustomUserSerializer

    def create(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():

            serializer.save()
            return Response({'message': 'User created successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class projectViewSet(viewsets.ModelViewSet):

    serializer_class = projectSerializer
    permission_classes = [CanCreateProjectPermission]

    def create(self, request, *args, **kwargs):
        request.data['projectCreator'] = request.user.id
        serializer = projectViewSet(data=request.data)
        if serializer.is_valid():   

            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



