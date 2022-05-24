from django.urls import path
from . import views

app_name ='movies'
urlpatterns = [
    # path('', views.movie, name='movie'),
    path('id/', views.movieid, name='movieid'),
    path('', views.index, name='index'),
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('recommend/otts/<int:ott_id>/', views.recommend_otts, name='recommend_otts'),
    path('recommend/directors/<int:director_id>/', views.recommend_directors, name='recommend_directors'),
    path('recommend/keywords/<int:keyword_id>/', views.recommend_keywords, name='recommend_keywords'),
]