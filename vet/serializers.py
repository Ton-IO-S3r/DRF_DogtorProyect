from rest_framework import serializers
from rest_framework.fields import ReadOnlyField
from rest_framework.views import APIView
from .models import Pet, PetDate, PetOwner


class PetOwnersListModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = PetOwner
    fields = ['id','first_name', 'last_name']


class PetOwnerModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = PetOwner
    fields = ['id','first_name', 'last_name','address','email', 'phone']


class PetsListModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pet
    fields = ['id', 'name', 'type']

class PetModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = Pet
    fields = ['id', 'name', 'type', 'owner']
  

class PetDatesModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = PetDate
    fields = ['id','datetime','pet']

class PetDateModelSerializer(serializers.ModelSerializer):
  class Meta:
    model = PetDate
    fields = ['id','datetime','pet','type']

class PetDateUpdateModelSerializer(serializers.ModelSerializer):
  pet = PetModelSerializer(read_only = True)
  class Meta:
    model = PetDate
    fields = ['datetime','type', 'pet']