from django.urls import path
from .views import PetOwnersListCreate, PetsList

urlpatterns = [
  path('owners/', PetOwnersListCreate.as_view(), name= 'owner_list'),
  path('pets/', PetsList.as_view(), name= 'pet_list'),
]