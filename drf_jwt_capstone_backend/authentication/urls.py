from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import RegisterView, UserDetail, UserList, CustomTokenObtainPairView, CustomTokenObtainPairRefreshView

urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', CustomTokenObtainPairRefreshView.as_view(),
         name='token_refresh'),
    path('register/', RegisterView.as_view(), name='register'),
    path('userid/', UserList.as_view(), name="userlist"),
    path('user/<int:pk>', UserDetail.as_view(), name='getuser'),
    path('username/<str:username>', UserDetail.as_view(), name='get_user_by_name'),
]
