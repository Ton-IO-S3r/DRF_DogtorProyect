from django.urls import path
from .views import (
  PetOwnerRetrieveUpdateDestroyAPIView,
  PetOwnersListCreateAPIView,
  PetRetreiveUpdateDestroyAPIView,
  PetsListCreateAPIView,
)

urlpatterns = [
  #Pet owners
  path('owners/', PetOwnersListCreateAPIView.as_view(), name= 'owner_list'),
  path(
    'owners/<int:pk>/',
    PetOwnerRetrieveUpdateDestroyAPIView.as_view(),
    name = 'owners_retrieve-update-destroy'
  ),
  # Pets
  path('pets/', PetsListCreateAPIView.as_view(), name= 'pet_list'),
  path('pets/<int:pk>/', PetRetreiveUpdateDestroyAPIView.as_view(), name = 'pet_details'),
]