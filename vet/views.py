from rest_framework import status, generics
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from django.shortcuts import get_object_or_404

#Modelos
from .models import Pet, PetDate, PetOwner

#Serializers
from .serializers import (
  PetDateModelSerializer,
  PetDateUpdateModelSerializer,
  PetDatesModelSerializer,
  PetOwnersListModelSerializer, 
  PetOwnerModelSerializer, 
  PetsListModelSerializer, 
  PetModelSerializer, 
)

# PETOWNERS VIEWS

class PetOwnersListCreateAPIView(generics.ListCreateAPIView):
  queryset = PetOwner.objects.all()
  serializer_class = PetOwnersListModelSerializer

  def get_queryset(self):

      first_name_filter = self.request.GET.get("first_name")
      filters = {}
      if first_name_filter:
          filters["first_name__icontains"] = first_name_filter

      return self.queryset.filter(**filters)

  def get_serializer_class(self):
      serializer_class = self.serializer_class
      if self.request.method == "POST":
          serializer_class = PetOwnerModelSerializer

      return serializer_class

class PetOwnersRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = PetOwner.objects.all()
  serializer_class = PetOwnerModelSerializer


# PET VIEWS

class PetsListCreateAPIView(generics.ListCreateAPIView):
  queryset = Pet.objects.all()
  serializer_class = PetsListModelSerializer

  def get_queryset(self):

      first_name_filter = self.request.GET.get("first_name")
      filters = {}
      if first_name_filter:
          filters["first_name__icontains"] = first_name_filter

      return self.queryset.filter(**filters)

  def get_serializer_class(self):
      serializer_class = self.serializer_class
      if self.request.method == "POST":
          serializer_class = PetModelSerializer

      return serializer_class

class PetsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = Pet.objects.all()
  serializer_class = PetModelSerializer

#PETS APPOINMENTS
class PetDatesListCreateAPIView(generics.ListCreateAPIView):
  queryset = PetDate.objects.all()
  serializer_class = PetDateModelSerializer
  def get_queryset(self):
      pet_filter = self.request.GET.get("pet_id")
      owner_filter =  self.request.GET.get("owner_id")
      filters = {}
      if pet_filter:
        filters["pet__in"] = pet_filter
      if owner_filter:
        filters["pet__owner__in"] = owner_filter

      return self.queryset.filter(**filters)

  def get_serializer_class(self):
      serializer_class = self.serializer_class
      if self.request.method == "POST":
          serializer_class = PetDateModelSerializer

      return serializer_class

class PetDatesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = PetDate.objects.all()
  serializer_class = PetDateUpdateModelSerializer