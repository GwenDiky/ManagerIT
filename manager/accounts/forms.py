from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from .models import Profile

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label="Имя",max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(label="Фамилия", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Почта",widget=forms.EmailInput(attrs={'class':'form-control'}))
    company = forms.CharField(label="Компания", widget=forms.TextInput(attrs={'class':'form-control'}))
    job_title = forms.CharField(label="Должность", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User 
        fields = ('first_name', 'last_name', 'username', 'email', 'company', 'job_title', 'password1', 'password2')
    def __init__(self, *args, **kwargs):
        super(RegisterUserForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password1'] != cd['password2']:
            raise forms.ValidationError('Пароли не совпадают.')
        return cd['password2']
    

class UserAEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

"UserEditForm позволит пользователям редактировать свое имя, фамилию и адрес электронной почты, которые являются атрибутами встроенной в Django модели User"

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'pgoto']


"ProfileEditForm позволит пользователям редактировать данные профиля, сохраненные в конкретно-прикладной модели Profile"