from django.urls import path
from tasks import views
urlpatterns = [
    path("home/", views.home_view),
    path("intro/", views.intro_page),
    path("datetime/", views.date_time),
    path("task/", views.task_page)
]