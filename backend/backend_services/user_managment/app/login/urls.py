from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('login/google/', views.google_login),
    path('login/42/', views.login_42),
    path('login/callback/', views.callback),
    path('login/refresh/', TokenRefreshView.as_view()),
    path('logout/', views.logout),
    path('whoami/', views.whoami),
    path('delete/user/', views.delete_user),
]
