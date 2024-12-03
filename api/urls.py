from django.urls import path 
from api import views

urlpatterns = [
    path('resume/', views.ProfileView.as_view(), name="profile"),
    path('list/', views.ProfileView.as_view(), name="list"),
]
