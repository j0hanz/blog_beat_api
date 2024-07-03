from django.urls import path
from . import views

urlpatterns = [
    path('profiles/', views.ProfileList.as_view(), name='profile-list'),
    path(
        'profiles/<int:pk>/',
        views.ProfileDetail.as_view(),
        name='profile-detail',
    ),
    path(
        'social-media-links/',
        views.SocialMediaLinkList.as_view(),
        name='social-media-link-list',
    ),
    path(
        'social-media-links/<int:pk>/',
        views.SocialMediaLinkDetail.as_view(),
        name='social-media-link-detail',
    ),
]
