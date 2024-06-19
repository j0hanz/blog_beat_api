from django.urls import path
from posts import views

urlpatterns = [
    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('bookmarks/', views.BookmarkList.as_view()),
    path('bookmarks/<int:pk>/', views.BookmarkDetail.as_view()),
]
