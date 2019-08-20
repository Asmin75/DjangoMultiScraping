from django.urls import path
from . import views

app_name = 'web_interface'

urlpatterns = [
    path('weblist/', views.WebListView.as_view()),
    path('search/', views.SearchView.as_view()),
    path('jsonlist/', views.jsonlistView),
]
