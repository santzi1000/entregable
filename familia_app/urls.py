from django.urls import path

from familia_app import views

app_name = "familia_app"
urlpatterns = [
    
    path("familiars", views.familiars, name="familiar-list")
]