from django.urls import path
from .views import (
  # PetOwnerRetrieveUpdateDestroyAPIView,
  # PetOwnersListCreateAPIView,
  # PetRetreiveUpdateDestroyAPIView,
  # PetsListCreateAPIView,
  PetOwnerRetreiveAPIView,
  PetOwnersListAPIView,
  PetsListAPIView,
  PetRetreiveAPIView,
)

urlpatterns = [
  # #Pet owners
  path('owners/', PetOwnersListAPIView.as_view(), name= 'owner_list'),
  # path('owners/', PetOwnersListCreateAPIView.as_view(), name= 'owner_list'),
  path(
    'owners/<int:pk>/',
    PetOwnerRetreiveAPIView.as_view(),
    name = 'owners_retrieve-update-destroy'
  ),
  # path(
  #   'owners/<int:pk>/',
  #   PetOwnerRetrieveUpdateDestroyAPIView.as_view(),
  #   name = 'owners_retrieve-update-destroy'
  # ),
  # # Pets
  path('pets/', PetsListAPIView.as_view(), name= 'pet_list'),
  path('pets/<int:pk>/', PetRetreiveAPIView.as_view(), name = 'pet_details'),
  # path('pets/', PetsListCreateAPIView.as_view(), name= 'pet_list'),
  # path('pets/<int:pk>/', PetRetreiveUpdateDestroyAPIView.as_view(), name = 'pet_details'),
]