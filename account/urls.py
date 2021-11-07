from django.urls import path
from django.contrib.auth.views import LogoutView, LoginView, \
    PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView

from account import views
from BoBSDB import settings

urlpatterns = [
    path('login/', views.signin, name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': settings.LOGOUT_REDIRECT_URL}, name='logout'),
    path('register/', views.signup, name="register"),
    path('activate/<uidb64>/<token>/', views.activate, name="activate"),
    path('password_reset/',
         PasswordResetView.as_view(template_name='registration/password_reset_form_.html',
                                   html_email_template_name='registration/password_reset_email_.html'),
         name='password_reset',
         ),
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

# TODO: в password_reset надо заменить стандартный шаблон на такой же, как 'registration/acc_active_email.html'
# Скопировать шаблон 'registration/acc_active_email.html', переименовать и отредачить для подтверждение регистрации:
# 1. чтобы туда правильно подставилась ссылка в нужное место
# 2. текст в нем немного переделать, чтобы подтверждению регистрации соответствовал

# Есть вот такой варик замены шаблона, он действительно работает, но как подставить в шаблон значения необходимые,
# я не понял
'''
path('password_reset/',
     PasswordResetView.as_view(template_name='registration/password_reset_form_.html',
     html_email_template_name='registration/acc_active_email.html'),
     name='password_reset',),
'''
