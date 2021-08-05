from rest_framework import generics, filters
from django_filters.rest_framework import DjangoFilterBackend

#Modelos
from .models import Pet, PetDate, PetOwner

#Serializers
from .serializers import (
  PetDatesListModelSerializer,
  PetDateUpdateModelSerializer,
  PetOwnersListModelSerializer, 
  PetOwnerModelSerializer, 
  PetsListModelSerializer, 
  PetModelSerializer, 
)

# PETOWNERS VIEWS

class PetOwnersListCreateAPIView(generics.ListCreateAPIView):
  queryset = PetOwner.objects.all()
  serializer_class = PetOwnersListModelSerializer
  filter_backends = [filters.SearchFilter, filters.OrderingFilter]
  search_fields = ['first_name','last_name']
  ordering_fields = ['email']
  # filterset_fields = ['first_name', 'last_name']

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
  serializer_class = PetDatesListModelSerializer
  filter_backends = [filters.SearchFilter]
  search_fields = ['pet__owner__first_name']
  # def get_queryset(self):
  #     pet_filter = self.request.GET.get("pet_id")
  #     owner_filter =  self.request.GET.get("owner_id")
  #     filters = {}
  #     if pet_filter:
  #       filters["pet__in"] = pet_filter
  #     if owner_filter:
  #       filters["pet__owner__in"] = owner_filter

  #     return self.queryset.filter(**filters)

  def get_serializer_class(self):
      serializer_class = self.serializer_class
      if self.request.method == "POST":
          serializer_class = PetDatesListModelSerializer

      return serializer_class

class PetDatesRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
  queryset = PetDate.objects.all()
  serializer_class = PetDateUpdateModelSerializer