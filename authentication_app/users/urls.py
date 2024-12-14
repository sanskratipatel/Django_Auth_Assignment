# from django.urls import path
# from django.contrib.auth import views as auth_views
# from . import views

# urlpatterns = [
#     path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('signup/', views.signup_view, name='signup'),
#     path('forgot-password/', auth_views.PasswordResetView.as_view(template_name='users/forgot_password.html'), name='forgot_password'),
#     path('change-password/', auth_views.PasswordChangeView.as_view(template_name='users/change_password.html'), name='change_password'),
#     path('dashboard/', views.dashboard_view, name='dashboard'),
#     path('profile/', views.profile_view, name='profile'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]

# from django.urls import path
# from . import views
# from django.contrib.auth import views as auth_views
# urlpatterns = [
#     path('login/', views.login_view, name='login'),
#     path('complete-profile/', views.complete_profile, name='complete_profile'),
#     # path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
#     path('signup/', views.signup_view, name='signup'),
#     path('forgot-password/', views.forgot_password, name='forgot_password'),
#     path('verify-otp/', views.verify_otp, name='verify_otp'),
#     path('reset-password/', views.reset_password_view, name='reset_password'),
#     path('change-password/', views.CustomPasswordChangeView.as_view(), name='change_password'), 
#     # path('user-profile', views.list_user_profiles, name='list_user_profiles'),  # Route for change password
#     path('dashboard/', views.dashboard_view, name='dashboard'),
#     path('profile/', views.profile_view, name='profile'),
#     path('logout/', auth_views.LogoutView.as_view(), name='logout'),
# ]

from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    # Authentication routes
    path('login/', views.login_view, name='login'),  # Custom login view
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),  # Logout redirect to login
    path('signup/', views.signup, name='signup'),
    path('forgot-password/', views.forgot_password, name='forgot_password'),
    path('verify-otp/', views.verify_otp, name='verify_otp'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('change-password/', views.CustomPasswordChangeView.as_view(), name='change_password'),

    # Dashboard and profile
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('profile/', views.profile_view, name='profile'),
    path('complete-profile/', views.complete_profile, name='complete_profile'),
]
