from django import forms
from django.contrib.auth.models import User
from .models import Profile


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')


class LoginForm(forms.Form):
    username = forms.CharField(label="用户名")
    password = forms.CharField(widget=forms.PasswordInput, label="密码")


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='密码',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='再次输入密码',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('两次密码输入不一致')
        return cd['password2']
