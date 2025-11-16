from .models import UserModel, SkillModel
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = UserModel
    fields = ['first_name', 'last_name', 'email', 'date_joined']

  
class SkillSerializer(serializers.ModelSerializer):
  class Meta:
    model = SkillModel
    fields = [
      'id',
      'user',
      'title',
      'level',
      'years_of_experience',
    ]