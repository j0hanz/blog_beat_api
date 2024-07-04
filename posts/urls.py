from django.urls import path
from . import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path(
        'posts/<int:pk>/favourite/',
        views.FavoritePost.as_view(),
        name='post-favourite',
    ),
]
