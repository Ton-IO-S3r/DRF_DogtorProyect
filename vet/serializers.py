from rest_framework import serializers

class PetOwnersListSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  first_name = serializers.CharField()    
  last_name = serializers.CharField()

class PetsListSerializer(serializers.Serializer):
  id = serializers.IntegerField()
  name = serializers.CharField()    
  type = serializers.CharField()
  owner = serializers.CharField()