from django.urls import path

from core import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("experience/", views.experience, name="experience"),
    path("contact/", views.contact, name="contact"),
    path("projects/", views.projects, name="projects"),

    path("projects/nextGenVoting", views.nextGenVoting, name="nextgenvoting"),
    path("projects/restaurantManagementSyetem", views.restaurantManagementSyetem, name="restaurantManagementSyetem"),

]
