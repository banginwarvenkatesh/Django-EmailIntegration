from django.urls import path
from . import views

urlpatterns = [

    path('email/', views.saveUser, name="eml_url"),

]