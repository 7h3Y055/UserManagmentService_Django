from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .views import *

urlpatterns = [
    path('login/google/', google_login),
    path('login/42/', login_42),
    path('login/callback/', callback),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('logout/', logout),
    path('whoami/', whoami),
    path('update-profile/', update_profile),
    path('delete/user/', delete_user),
    path('avatar/', avatar),
    path('search/', search),
    path('<int:user_id>', info),
    path('users/', get_user),
]
