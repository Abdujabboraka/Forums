from django.contrib.auth.models import User
from django import forms
from .models import Mavzu, Comment

class MavzuForm(forms.ModelForm):

    class Meta:
        fields = ['title', 'content', 'image']
        model = Mavzu
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mavzu Nomi'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mazmuni'}),
            'image' : forms.FileInput()
        }

class RegisterForm(forms.ModelForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password'
    }))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control', 'placeholder': 'Password again'
    }))
    remember_me = forms.BooleanField(required=False, widget=forms.CheckboxInput(attrs={
        'class': 'form-control'
    }))

    class Meta:
        model = User
        fields = ['username','first_name', 'last_name', 'email', 'password', 'password2', 'remember_me']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ism'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'familya'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
        }

class LoginForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
        }

class CommentForm(forms.Form):
    content = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Komentniyatni yoqing'}), max_length=1000)
