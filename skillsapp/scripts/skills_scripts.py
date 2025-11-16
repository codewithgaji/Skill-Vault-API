from skillsapp.models import UserModel, SkillModel

def run():
  users =  list(UserModel.objects.all())

  if len(users) < 3:
    print("Not enough users in the database. Add at least 3 users.")
    return
  user1, user2, user3 = users[0], users[1], users[2]

  SkillModel.objects.create(
    user=user1,
    title="Python",
    level=SkillModel.SkillLevel.ADVANCED,
    years_of_experience=3
  )

  SkillModel.objects.create(
      user=user1,
      title="Django",
      level=SkillModel.SkillLevel.INTERMEDIATE,
      years_of_experience=2
  )

  SkillModel.objects.create(
      user=user2,
      title="React",
      level=SkillModel.SkillLevel.INTERMEDIATE,
      years_of_experience=2
  )

  SkillModel.objects.create(
      user=user2,
      title="Figma",
      level=SkillModel.SkillLevel.BEGINNER,
      years_of_experience=1
  )

  SkillModel.objects.create(
      user=user3,
      title="MongoDB",
      level=SkillModel.SkillLevel.BEGINNER,
      years_of_experience=1
  )
  print("User added Successfully")