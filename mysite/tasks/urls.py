from django.urls import path
from tasks import views
urlpatterns = [
    path("home/", views.home_view),
    path("welcome/", views.welcome_page)

]