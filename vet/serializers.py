from rest_framework import serializers
from .models import Pet, PetOwner

class PetOwnersListSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  first_name = serializers.CharField()    
  last_name = serializers.CharField()

class PetOwnerSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  first_name = serializers.CharField(max_length = 255)    
  last_name = serializers.CharField(max_length = 255)
  address = serializers.CharField()
  email = serializers.EmailField()
  phone = serializers.CharField()

  def create(self, validated_data):
    return PetOwner.objects.create(**validated_data)


class PetsListSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()    
  type = serializers.CharField()

class PetSerializer(serializers.Serializer):
  id = serializers.ReadOnlyField()
  name = serializers.CharField(max_length = 255)
  type = serializers.CharField(max_length = 50)
  owner = serializers.PrimaryKeyRelatedField(queryset = PetOwner.objects.all())
  def create(self, validated_data):
    return Pet.objects.create(**validated_data)