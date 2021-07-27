from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name="home"),
    path('explore/', views.explore, name="explore"),
    path('search/<str:search_text>', views.search, name="search"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('update/<int:id>', views.update, name="update"),
]