from django.urls import path
from django.contrib.auth import views as auth_views
from .views import register  # custom view for registration

urlpatterns = [
    # existing URLs…
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', register, name='register'),
]
