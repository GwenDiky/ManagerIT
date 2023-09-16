from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from django import forms 
from .models import Profile
from phonenumber_field.formfields import PhoneNumberField
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class RegisterUserForm(UserCreationForm):
    first_name = forms.CharField(label="Имя", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    surname = forms.CharField(label="Отчество", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}), required=False)
    last_name = forms.CharField(label="Фамилия", max_length=50, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Почта",widget=forms.EmailInput(attrs={'class':'form-control'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}), max_length=300, label='Описание')
    company = forms.CharField(label="Компания", widget=forms.TextInput(attrs={'class':'form-control'}))
    country = forms.CharField(label="Страна", widget=forms.TextInput(attrs={'class':'form-control'}))
    city = forms.CharField(label="Город", widget=forms.TextInput(attrs={'class':'form-control'}))
    job_title = forms.CharField(label="Должность", widget=forms.TextInput(attrs={'class':'form-control'}))
    phone_number = PhoneNumberField(label='Номер телефона:', region='BE', widget=PhoneNumberPrefixWidget(attrs={'class':'form-control'},
            country_choices=[
                 ("BEL", "Беларусь"),
                 ("RU", "Россия"),
            ],
        ),
        )
    experience_years = forms.DecimalField(label='Опыт', widget=forms.NumberInput(attrs={'class':'form-control', 'size':10}),
                                          help_text='Опыт работы должен быть реальным. В годах' )
    experience = forms.CharField(label='Опыт работы', widget=forms.Textarea(attrs={'class':'form-control'}), max_length=300)
    education = forms.CharField(label='Образование', widget=forms.Textarea(attrs={'class':'form-control'}), max_length=300)
    contacts = forms.CharField(label='Соцсети', widget=forms.Textarea(attrs={'class':'form-control'}), max_length=300)

    class Meta:
        model = User 
        fields = ('first_name', 'surname', 'last_name', 'username', 'email', 'company', 'country', 'city', 'job_title', 'experience_years', 'password1', 'password2', 'education', 'contacts', 'description')
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

    def clean_experience_years(self):
        data = self.cleaned_data['experience_years']
        if data < 0:
            raise forms.ValidationError('Опыт работы не может быть отрицательным.')
        elif data > 100:
            raise forms.ValidationError('Введите реальный опыт работы.')
        return data
    

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super(UserEditForm, self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs['class'] = 'form-control'
        self.fields['last_name'].widget.attrs['class'] = 'form-control'
        self.fields['email'].widget.attrs['class'] = 'form-control'


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

    def __init__(self, *args, **kwargs):
        super(ProfileEditForm, self).__init__(*args, **kwargs)
        self.fields['date_of_birth'].widget.attrs['class'] = 'form-control'
        self.fields['photo'].widget.attrs['class'] = 'form-control'


"ProfileEditForm позволит пользователям редактировать данные профиля, сохраненные в конкретно-прикладной модели Profile"