# from django.contrib.auth.views import LoginView as BaseLoginView
# from django.contrib.auth.views import LogoutView as BaseLogoutView
import random

from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, UpdateView

from users.forms import UserProfileForm, UserRegisterForm
from users.models import User
from users.services import send_new_password_mail


# class LoginView(BaseLoginView):
#     template_name = 'users/login.html'


class RegisterView(CreateView):
    model = User
    form_class = UserRegisterForm
    template_name = 'users/register.html'
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        self.object = form.save()
        send_mail(
            subject='Поздравляем с регистрацией!',
            message='Вы зарегистрировались на платформе Shelter. Бобро пожаловать!',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[self.object.email]
        )
        return super().form_valid(form)


class ProfileView(LoginRequiredMixin, UpdateView):
    model = User
    form_class = UserProfileForm
    success_url = reverse_lazy('users:profile')

    def get_object(self, queryset=None):
        return self.request.user


@login_required
def create_password(request):
    new_password = ''.join([str(random.randint(0, 9)) for _ in range(12)])
    send_new_password_mail(request.user.email, new_password)
    request.user.set_password(new_password)
    request.user.save()
    return redirect(reverse('dogs:index'))
