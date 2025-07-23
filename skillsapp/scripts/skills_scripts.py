from skillsapp.models import UserModel, SkillModel

from skillsapp.serializers import UserSerializer

def run():
    print("=== DEBUGGING SERIALIZER ===")
    
    # Test single user serialization
    user = UserModel.objects.first()
    print(f"Raw user object: {user}")
    print(f"User ID: {user.id}")
    print(f"User attributes: {vars(user)}")
    
    # Test serializer with single user
    serializer = UserSerializer(user)
    print(f"Single user serialized: {serializer.data}")
    print(f"Serializer fields: {serializer.fields}")
    
    # Test serializer with all users
    all_users = UserModel.objects.all()
    serializer_many = UserSerializer(all_users, many=True)
    print(f"All users serialized: {serializer_many.data}")
    
    # Check if 'id' is in the serialized data
    serialized_data = serializer_many.data
    if serialized_data:
        first_user_data = serialized_data[0]
        print(f"First user keys: {list(first_user_data.keys())}")
        print(f"Does first user have 'id'?: {'id' in first_user_data}")
        
        if 'id' in first_user_data:
            print(f"ID value: {first_user_data['id']}")
        else:
            print("❌ ID field is missing from serialized data!")
    
    print("=== END DEBUG ===")




















  # users =  list(UserModel.objects.all())

  # if len(users) < 3:
  #   print("Not enough users in the database. Add at least 3 users.")
  #   return
  # user1, user2, user3 = users[0], users[1], users[2]

  # SkillModel.objects.create(
  #   user=user1,
  #   title="Python",
  #   level=SkillModel.SkillLevel.ADVANCED,
  #   years_of_experience=3
  # )

  # SkillModel.objects.create(
  #     user=user1,
  #     title="Django",
  #     level=SkillModel.SkillLevel.INTERMEDIATE,
  #     years_of_experience=2
  # )

  # SkillModel.objects.create(
  #     user=user2,
  #     title="React",
  #     level=SkillModel.SkillLevel.INTERMEDIATE,
  #     years_of_experience=2
  # )

  # SkillModel.objects.create(
  #     user=user2,
  #     title="Figma",
  #     level=SkillModel.SkillLevel.BEGINNER,
  #     years_of_experience=1
  # )

  # SkillModel.objects.create(
  #     user=user3,
  #     title="MongoDB",
  #     level=SkillModel.SkillLevel.BEGINNER,
  #     years_of_experience=1
  # )
  # print("User added Successfully")