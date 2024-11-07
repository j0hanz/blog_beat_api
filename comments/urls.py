from django.urls import path

from comments import views

urlpatterns = [
    path('', views.CommentList.as_view()),
    path('<int:pk>/', views.CommentDetail.as_view()),
]
