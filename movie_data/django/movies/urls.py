from django.urls import path
from . import views

app_name ='movies'
urlpatterns = [
    # path('', views.movie, name='movie'),
    path('id/', views.movieid, name='movieid'),
    path('', views.index, name='index'),
]