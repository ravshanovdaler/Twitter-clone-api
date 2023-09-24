from django.urls import path
from . import views


urlpatterns = [
    path('all/', views.PostListView.as_view()),
    path('create/', views.PostCreateView.as_view()),
    path('<int:pk>/', views.PostDeleteUpdateView.as_view()),
    path('like/', views.LikeCreateView.as_view()),
    path('like/<int:pk>/remove', views.LikeDeleteView.as_view()),
    path('comments/', views.CommentCreateView.as_view()),
]
