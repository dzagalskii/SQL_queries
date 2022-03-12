from random import randint
from django.contrib.auth import get_user_model
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import SignupForm, LoginForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import send_mail
from django.contrib.auth import authenticate, login
from django.conf import settings
from dbserver.Core.Constants import DATA_SCHEMAS


def signin(request):
    if not request.user.is_authenticated:
        my_errors = []
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                cd = form.cleaned_data
                user = authenticate(username=cd['email'], password=cd['password'])
                if user is not None:
                    if user.is_active:
                        login(request, user)
                        return HttpResponseRedirect('/queries')
                    else:
                        my_errors.append('Данный аккаунт не активирован.')
                else:
                    my_errors.append('Неправильный логин или пароль.')
        else:
            form = LoginForm()
        return render(request, 'registration/login.html', {'form': form, 'errors': my_errors})
    else:
        return HttpResponseRedirect('/queries')


def signup(request):
    if not request.user.is_authenticated:
        my_errors = []
        if request.method == 'POST':
            form = SignupForm(request.POST)
            if form.is_valid():
                if '@edu.spbstu.ru' in form.cleaned_data.get('email'):
                    user = form.save(commit=False)
                    user.is_active = False
                    user.data_schemas = '{} {} {}'.format(DATA_SCHEMAS[randint(0, 2)],
                                                          DATA_SCHEMAS[randint(0, 2)],
                                                          DATA_SCHEMAS[randint(0, 2)], )
                    user.save()
                    current_site = get_current_site(request)
                    mail_subject = 'Активация аккаунта SQL Queries'
                    domain = current_site.domain
                    uid = urlsafe_base64_encode(force_bytes(user.pk))
                    token = account_activation_token.make_token(user)
                    activate_link = 'http://{domain}/account/activate/{uid}/{token}'.format(
                        domain=domain,
                        uid=uid,
                        token=token,
                    )
                    html_message = render_to_string('registration/acc_active_email.html', {
                        'activate_link': activate_link,
                        'user': user,
                    })
                    destination_email = form.cleaned_data.get('email')
                    send_mail(subject=mail_subject,
                              message=None,
                              from_email=settings.DEFAULT_FROM_EMAIL,
                              recipient_list=[destination_email],
                              html_message=html_message)
                    return render(request, 'registration/register_done.html')
                else:
                    my_errors.append('Адрес электронной почты должен быть с доменом @edu.spbstu.ru')
        else:
            form = SignupForm()
        for error_field in form.errors:
            for error in form.errors[error_field]:
                my_errors.append(error)
        return render(request, 'registration/register.html', {'form': form, 'errors': my_errors})
    else:
        return HttpResponseRedirect('/queries')


def activate(request, uidb64, token):
    if not request.user.is_authenticated:
        User = get_user_model()
        try:
            uid = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=uid)
        except(TypeError, ValueError, OverflowError, User.DoesNotExist):
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            return render(request, 'registration/register_complete.html')
        else:
            return render(request, 'registration/register_unsuccessfully.html')
    else:
        return HttpResponseRedirect('/queries')
