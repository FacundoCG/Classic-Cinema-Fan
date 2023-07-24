from django.urls import path
from .views import HomeView, MovieList, MovieCreate, MovieDelete, MovieUpdate

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('movie_list/', MovieList.as_view(), name="movie-list"),
    path('movie_create/', MovieCreate.as_view(), name="movie-create"),
    path('movie_update/<int:pk>/', MovieUpdate.as_view(), name="movie-update"),
    path('movie_delete/<int:pk>/', MovieDelete.as_view(), name="movie-delete"),    
]
