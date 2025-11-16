from django.shortcuts import render
from .models import SkillModel, UserModel
from .serializers import UserSerializer, SkillSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpRequest
from django.shortcuts import get_object_or_404
from rest_framework import status




# Create your views here.

# Create a Data (C)
@api_view(http_method_names=["POST"])
def create_skill(request:Request):
  if request.method == "POST":
    skill_data = request.data
    data_serializer = SkillSerializer(data=skill_data)

    if data_serializer.is_valid():
      data_serializer.save()
      response = {"Message": "Skill created successfully",
                  "Skill": data_serializer.data}
      
      return Response(data=response, status=status.HTTP_201_CREATED)
    
    response = {"Message": "Data Not valid",
                "Data": data_serializer.errors}

    return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
  

# Read Data (R)
@api_view(http_method_names=["GET"])
def read_skills(request:Request):
  skills = SkillModel.objects.all()
  skills_serializer = SkillSerializer(instance=skills, many=True)
  response  = {
    "Message": "This is all the skills",
    "Skills": skills_serializer.data
  }

  return Response(data=response, status=status.HTTP_200_OK)



# Read a single Data
@api_view(http_method_names=["GET"])
def view_skill(request:Request, skill_id:int):
  skill = get_object_or_404(SkillModel, pk=skill_id)
  serializer = SkillSerializer(instance = skill)
  response = {"Message": "This is the skill",
              "Skill": serializer.data}
  return Response(data=response, status=status.HTTP_200_OK)




# Update Skills (U)
@api_view(http_method_names=["PUT"])
def update_skills(request:Request, skill_id:int):
  skill = get_object_or_404(SkillModel, pk=skill_id)
  skill_modifier = request.data
  serializer = SkillSerializer(instance=skill, data=skill_modifier)
  if serializer.is_valid():
    serializer.save()
    response = {"Message": "Skill Updated Successfully", 
                "SKill": serializer.data}
    return Response(data=response, status=status.HTTP_202_ACCEPTED)
  
  response = {"Message": "Update Failed",
            "Error": serializer.errors}
  return Response(data=response, status=status.HTTP_400_BAD_REQUEST)


# Delete a Skill (D)
@api_view(http_method_names=["DELETE"])
def delete_skill(request:Request, skill_id:int):
  skill = get_object_or_404(SkillModel, pk=skill_id)

  skill.delete()
  response = {"Message": "Skill Deleted Successfully"}

  return Response(data=response, status=status.HTTP_410_GONE)

@api_view(["POST"])
def create_user(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({"message": "User created", "data": serializer.data}, status=201)
    return Response(serializer.errors, status=400)


@api_view(["GET"])
def get_users(request):
    users = UserModel.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


def about(request):
   return render(request, 'about.html')

def skillvault(request):
  return render(request, 'index.html')