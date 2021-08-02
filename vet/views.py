from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import get_object_or_404

#Modelos
from .models import Pet, PetOwner

#Serializers
from .serializers import PetOwnersListSerializer, PetOwnerSerializer, PetsListSerializer, PetSerializer

# Create your views here.
class PetOwnersListCreate(APIView):
  """
    View to list all pet owners in the system
  """
  serializer_class = PetOwnersListSerializer
  def get(self, request):
    owners_queryset = PetOwner.objects.all()
    serializer = self.serializer_class(owners_queryset, many = True)
    return Response(data=serializer.data)  
  
  def post(self, request):
    serializer = PetOwnerSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    created_instance = serializer.save()
    print(created_instance.__dict__)
    return Response({})

class PetsListCreate(APIView):
  """
    View to list all pets in the system
  """
  serializer_class = PetsListSerializer
  def get(self, request):
    pets_queryset = Pet.objects.all()
    serializer = self.serializer_class(pets_queryset, many = True)
    return Response(data=serializer.data) 
  
  def post(self, request):
    serializer = PetSerializer(data = request.data)
    serializer.is_valid(raise_exception = True)
    created_instance = serializer.save()
    print(created_instance.__dict__)
    return Response({})

class PetOwnerDetailAPIView(APIView):
  """
    View to show details of selected owner in the system
  """
  serializer_class = PetOwnerSerializer
  def get(self, request, pk):
    owner_queryset = get_object_or_404(PetOwner, id=pk)
    serializer = self.serializer_class(owner_queryset)
    return Response(data=serializer.data)

class PetDetailAPIView(APIView):
  """
    View to show details of selected pet in the system
  """
  serializer_class = PetSerializer
  def get(self, request, pk):
    pet_queryset = get_object_or_404(Pet, id=pk)
    serializer=self.serializer_class(pet_queryset)
    return Response(data = serializer.data)