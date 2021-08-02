from django.urls import path
from .views import PetDetailAPIView, PetOwnerDetailAPIView, PetOwnersListCreate, PetsListCreate

urlpatterns = [
  path('owners/', PetOwnersListCreate.as_view(), name= 'owner_list'),
  path('owners/<int:pk>/', PetOwnerDetailAPIView.as_view(), name = 'owner_details'),
  path('pets/', PetsListCreate.as_view(), name= 'pet_list'),
  path('pets/<int:pk>/', PetDetailAPIView.as_view(), name = 'pet_details'),
]