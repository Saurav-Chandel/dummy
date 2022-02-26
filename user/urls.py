from django.contrib import admin
from django.urls import path,include
from user import views

app_name = "user"

urlpatterns = [
    path('admin/', admin.site.urls),
    path("auth/api/v1/signup/", views.SignUpView.as_view(), name="signup"),
    path("auth/api/v1/login/", views.LoginView.as_view(), name="login"),
    # path("profile/api/v1/create/", views.CreateProfile.as_view(), name="profile"),
    # path("profile/api/v1/list/", views.GetAllProfile.as_view(), name="profile"),
    # path("profile/api/v1/update/<int:pk>/", views.UpdateProfile.as_view(), name="profile"),
    # path("profile/api/v1/get/<int:pk>/", views.GetProfile.as_view(), name="profile"),
    path(
        "auth/api/v1/forgot-password-email/",
        views.RequestPasswordResetEmailView.as_view(),
        name="forgot-password-email",
    ),
    path(
        "auth/api/v1/forgot-password/<uidb64>/<token>/",
        views.PasswordTokenCheckAPIView.as_view(),
        name="forgot-password-confirm",
    ),
    path(
        "auth/api/v1/forgot-password-complete/",
        views.SetNewPasswordAPIView.as_view(),
        name="password-reset-complete",
    ),
]