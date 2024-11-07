from django.urls import path

from . import views

urlpatterns = [
    path('', views.PostList.as_view()),
    path('<int:pk>/', views.PostDetail.as_view()),
    path(
        '<int:pk>/favourite/',
        views.FavoritePost.as_view(),
    ),
]
