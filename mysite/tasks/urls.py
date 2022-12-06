from django.urls import path
from tasks import views
urlpatterns = [
    path("home/", views.home_view),
    path("intro/", views.intro_page),
    path("datetime/", views.date_time),
    path("task/", views.task_page),
    path("task/create/", views.create_task),
    path("task/getall/", views.get_all_tasks),
    path("task/get_tasks/", views.get_tasks),
    path("task/<int:task_id>/update/", views.update_task)
]