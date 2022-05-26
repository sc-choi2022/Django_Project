from django.urls import path
from . import views

app_name = 'community'
urlpatterns = [
    # articles
    path('', views.article_list),
    path('<int:article_id>/', views.article_detail),
    path('<int:article_id>/like/', views.like_article),
    # comments
    path('<int:article_id>/comments/', views.create_comment),
    path('<int:article_id>/comments/<int:comment_id>/', views.comment_detail)
]