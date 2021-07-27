from django.urls import path,include
from . import views

urlpatterns = [
    path('', include("django.contrib.auth.urls")),
    path('', views.landing_page, name="landing_page"),
    path('signup/', views.signup, name="signup"),
    path('', include("main.urls")),
    ]
