from django.db import models

# Create your models here.

class UserModel(models.Model):
  first_name = models.CharField(max_length=50)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(unique=True)
  date_joined = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return f"{self.first_name} {self.last_name}"


class SkillModel(models.Model):
  class SkillLevel(models.TextChoices):
    BEGINNER = 'BEGINNER', 'Beginner'
    INTERMEDIATE = 'INTERMIDIATE', 'Intermediate'
    ADVANCED = 'ADVANCED', 'Advanced'

  user = models.ForeignKey(UserModel, related_name='skills', on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  level = models.CharField(max_length= 20, choices=SkillLevel.choices)
  years_of_experience = models.PositiveIntegerField()
  last_updated = models.DateTimeField(auto_now=True)

  def __str__(self):
    return f"{self.title} {self.level}"