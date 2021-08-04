from django.urls import path
from .views import (
  PetDatesListCreateAPIView,
  PetDatesRetrieveUpdateDestroyAPIView,
  PetOwnersListCreateAPIView,
  PetOwnersRetrieveUpdateDestroyAPIView,
  PetsListCreateAPIView,
  PetsRetrieveUpdateDestroyAPIView,
  
)

urlpatterns = [
  # #Pet owners
  path('owners/', PetOwnersListCreateAPIView.as_view(), name= 'owner_list-create'),
  path('owners/<int:pk>', PetOwnersRetrieveUpdateDestroyAPIView.as_view(), name= 'owners_retrieve-update-destroy'),
  
  # # Pets
  path('pets/', PetsListCreateAPIView.as_view(), name= 'pet_list-create'),
  path('pets/<int:pk>', PetsRetrieveUpdateDestroyAPIView.as_view(), name= 'pets_retrieve-update-destroy'),

  # # Pet Dates
  path('dates/', PetDatesListCreateAPIView.as_view(), name= 'petdates_list-create'),
  path('dates/<int:pk>', PetDatesRetrieveUpdateDestroyAPIView.as_view(), name= 'petdates_retrive-update.destroy'),
]