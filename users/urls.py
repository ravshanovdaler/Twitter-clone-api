from django.urls import path
from .views import SignupView,UserListView,FollowView,UserInfoView


urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('list/', UserListView.as_view()),
    path('follow/', FollowView.as_view()),
    path('<str:username>/', UserInfoView.as_view())
]
