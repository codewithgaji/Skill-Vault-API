from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("create/", views.create_skill, name="CreateSkill"),
    path("skills_set/", views.read_skills, name="skills_set"),
    path("update_skill/<int:skill_id>/", views.update_skills, name="update_skills"),
    path("delete_skill/<int:skill_id>/", views.delete_skill, name="delete_skill"),
    path("skillvault/", views.skillvault, name="skillvault"),
    path("create_user/", views.create_user, name="create_user"),
    path("get_users/", views.get_users, name="get_users"),
    path("skillvault/about/", views.about, name="about")
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)