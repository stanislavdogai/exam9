from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from accounts.views import register_view, ProfileDetailView, ProfileUserDetailView

app_name = 'accounts'

urlpatterns = [
    path('login/', LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('registration/', register_view, name='registration'),
    path('profile/<int:pk>/', ProfileDetailView.as_view(), name='profile'),
    path('profile/user/<int:pk>/', ProfileUserDetailView.as_view(), name='user_profile')
]