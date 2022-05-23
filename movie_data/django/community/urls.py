from django.urls import path
from . import views

app_name = 'community'

urlpatterns = [
    # articles
    path('', views.article_list),
    path('<int:article_pk>/', views.article_detail),
    path('<int:article_pk>/like/', views.like_article),
    # comments
    path('<int:article_pk>/comments/', views.create_comment),
    path('<int:article_pk>/comments/<int:comment_pk>/', views.comment_detail)
]