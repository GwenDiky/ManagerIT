from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from .models import Profile

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    surname = forms.CharField(label="Отчество", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    last_name = forms.CharField(label="Фамилия", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Почта",widget=forms.EmailInput(attrs={'class':'form-control'}))
    company = forms.CharField(label="Компания", widget=forms.TextInput(attrs={'class':'form-control'}))
    country = forms.CharField(label="Страна", widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(label="Город", widget=forms.TextInput(attrs={'class':'form-control'}))
    job_title = forms.CharField(label="Должность", widget=forms.TextInput(attrs={'class':'form-control'}))
    class Meta:
        model = User 
        fields = ('first_name', 'surname', 'last_name', 'username', 'email', 'company', 'country', 'city', 'job_title', 'password1', 'password2')
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
    

    def clean_email(self):
        data = self.cleaned_data['email']
        if User.objects.filter(email=data).exists():
            raise forms.ValidationError('Адрес электронный почты уже используется.')
        return data 
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def clean_email(self):
        data = self.cleaned_data['email']
        qs = User.objects.exclude(id = self.instance.id).filter(email=data)
        if qs.exists():
            raise forms.ValidationError('Адрес электронной почты уже используется.')
        return data

"UserEditForm позволит пользователям редактировать свое имя, фамилию и адрес электронной почты, которые являются атрибутами встроенной в Django модели User"

class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['date_of_birth', 'photo']


"ProfileEditForm позволит пользователям редактировать данные профиля, сохраненные в конкретно-прикладной модели Profile"