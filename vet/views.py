from rest_framework import status
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import get_object_or_404

#Modelos
from .models import Pet, PetOwner

#Serializers
from .serializers import (
  PetOwnersListSerializer, 
  PetOwnerSerializer,
  PetUpdateSerializer, 
  PetsListSerializer, 
  PetSerializer, 
  PetOwnerUpdateSerializer
)

# Create your views here.
class PetOwnersListCreateAPIView(APIView):
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
    serialized_instance = PetOwnerSerializer(created_instance)
    return Response(serialized_instance.data, status= status.HTTP_201_CREATED)

class PetsListCreateAPIView(APIView):
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
    serialized_instance = PetSerializer(created_instance)
    return Response(serialized_instance.data, status= status.HTTP_201_CREATED)

class PetOwnerRetrieveUpdateDestroyAPIView(APIView):
  """
    View to show details of selected owner in the system
  """
  serializer_class = PetOwnerSerializer
  def get(self, request, pk):
    owner_queryset = get_object_or_404(PetOwner, id=pk)
    serializer = self.serializer_class(owner_queryset)
    return Response(data=serializer.data)
  
  def patch(self, request, pk):
    owner = get_object_or_404(PetOwner, id=pk)
    serializer = PetOwnerUpdateSerializer(instance=owner, data=request.data)
    serializer.is_valid(raise_exception=True)
    updated_instance = serializer.save()
    serialized_instance = self.serializer_class(updated_instance)
    return Response(serialized_instance.data)
  
  def delete(self, request, pk):
    owner = get_object_or_404(PetOwner, id=pk)
    owner.delete()
    return Response(status.HTTP_204_NO_CONTENT)

class PetRetreiveUpdateDestroyAPIView(APIView):
  """
    View to show details of selected pet in the system
  """
  serializer_class = PetSerializer
  def get(self, request, pk):
    pet_queryset = get_object_or_404(Pet, id=pk)
    serializer=self.serializer_class(pet_queryset)
    return Response(data = serializer.data)
  
  def patch(self, request, pk):
    pet = get_object_or_404(Pet, id=pk)
    serializer = PetUpdateSerializer(instance = pet, data=request.data)
    serializer.is_valid(raise_exception = True)
    updated_instance = serializer.save()
    serialized_instance = self.serializer_class(updated_instance)
    return Response(serialized_instance.data)
  
  def delete(self, request, pk):
    pet = get_object_or_404(Pet, id=pk)
    pet.delete()
    return Response(status.HTTP_204_NO_CONTENT)