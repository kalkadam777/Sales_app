from django.shortcuts import render
from django.urls import reverse_lazy
from rest_framework import viewsets, permissions
from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView
from django.contrib.auth.views import PasswordChangeView

from .forms import LoginUserForm, RegisterUserForm, ProfileUserForm, UserPasswordChangeForm
from .serializers import UserSerializer
from django.contrib.auth.views import LoginView

User = get_user_model()

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'users/login.html'
    extra_context = {'title':'Авторизация'}
    
def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return render(request, 'users/register_done.html')
    else:
        form = RegisterUserForm()
    return render(request, 'users/register.html', {'form': form})

class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm
    template_name = 'users/profile.html'
    extra_context = {'title':'Профиль пользователя'}
    
    def get_success_url(self):
        return reverse_lazy('profile')
    
    def get_object(self, queryset=None):
        return self.request.user
    
class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'users/password_change_form.html'
    success_url = reverse_lazy('password_change_done')
    
    
    