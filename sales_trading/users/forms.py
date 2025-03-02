from django.contrib.auth.forms import AuthenticationForm
from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label= 'Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label= 'Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    
class RegisterUserForm(forms.ModelForm):
    username = forms.CharField(label= 'Логин')
    password = forms.CharField(label= 'Пароль', widget=forms.PasswordInput())
    password2 = forms.CharField(label= 'Повторите пароль', widget=forms.PasswordInput())
    
    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name', 'last_name', 'password', 'password2']
        labels = {
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
    def clean_password2(self):
        data = self.cleaned_data
        if data['password'] != data['password2']:
            raise forms.ValidationError('Пароли не совпадают')
        return data['password']
    
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Пользователь с таким email уже зарегистрирован')
        return email
    
    
class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True,label= 'Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(disabled=True,label= 'Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    
    class Meta:
        model = get_user_model()
        fields = ['username','email','first_name', 'last_name']
        labels = {
            'email': 'Email',
            'first_name': 'Имя',
            'last_name': 'Фамилия',
        }
        widjets = {
            
            'first_name': forms.TextInput(attrs={'class': 'form-input'}),
            'last_name': forms.TextInput(attrs={'class': 'form-input'}),
        }