from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from django.urls.base import reverse_lazy


app_name = 'users'

urlpatterns = [
    path("", views.index, name='index'),
    # Register
    path('register/', views.register, name='register'),
    #  login and logout
    path("login/", views.login_user, name='login'),
    path("logout/", auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # password change
    path("password_change/", auth_view.PasswordChangeView.as_view(success_url=reverse_lazy(
        'users:password_change_done'), template_name='users/password_change_form.html'), name='password_change'),
    path("password_change/done/", auth_view.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'), name='password_change_done'),
]
