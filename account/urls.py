from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from account import views
from BoBSDB import settings

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('register/', views.signup, name="register"),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('password_reset/',
         PasswordResetView.as_view(template_name='registration/password_reset_form_.html'),
         name='password_reset'),
    path('password_reset_done/',
         PasswordResetDoneView.as_view(template_name='registration/password_reset_done_.html'),
         name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm_.html'),
         name='password_reset_confirm'),
    path('password_reset_complete/',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete_.html'),
         name='password_reset_complete')
]
