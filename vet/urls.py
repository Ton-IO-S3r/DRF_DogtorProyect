from django.urls import path
from .views import PetOwnersList, PetsList

urlpatterns = [
  path('owners/', PetOwnersList.as_view(), name= 'owner_list'),
  path('pets/', PetsList.as_view(), name= 'pet_list'),
]