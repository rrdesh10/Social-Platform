from django.urls import path, reverse_lazy
from django.contrib.auth import views as auth_view
from . import views


app_name = 'users'

urlpatterns = [
    path("", views.index, name='index'),
    #  login and logout
    path("login/", views.login_user, name='login'),
    path("logout/", auth_view.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    # password change
    path("password_change/", auth_view.PasswordChangeView.as_view(success_url=reverse_lazy(
        'users:password_change_done'), template_name='users/password_change_form.html'), name='password_change'),
    path("password_change/done/", auth_view.PasswordChangeDoneView.as_view(
        template_name='users/password_change_done.html'), name='password_change_done'),
    # password reset
    path("password_reset/", auth_view.PasswordResetView.as_view(success_url=reverse_lazy(
        'users:password_reset_done'), template_name='users/password_reset_form.html'), name='password_reset'),
    path("password_reset/done/", auth_view.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    # password reset confirm
    path("password_reset/<uid64>/<token>/", auth_view.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),

]
