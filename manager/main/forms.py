from django.forms import ModelForm
from .models import Task, Comment
from django import forms



class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super(TaskForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs['class'] = 'form-control'
        self.fields['slug'].widget.attrs['class'] = 'form-control'
        self.fields['tags'].widget.attrs['class'] = 'form-control'
        self.fields['content'].widget.attrs['class'] = 'form-control'
        self.fields['image'].widget.attrs['class'] = 'form-control'
        self.fields['type'].widget.attrs['class'] = 'form-control'
        self.fields['person'].widget.attrs['class'] = 'form-control'
        self.fields['company'].widget.attrs['class'] = 'form-control'
        self.fields['status'].widget.attrs['class'] = 'form-control'
        self.fields['complete_date'].widget.attrs['class'] = 'form-control'
    

class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=50, label="Имя")
    email = forms.EmailField(label="Электронная почта отправителя")
    to = forms.EmailField(label="Электронная почта получателя")
    comments = forms.CharField(required=False, widget=forms.Textarea, label="Комментарии")

class CommentForm(forms.ModelForm):
    name = forms.CharField(label="Имя", max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(label="Почта", widget=forms.EmailInput(attrs={'class':'form-control'}))
    body = forms.CharField(label="Текст", widget=forms.Textarea(attrs={'class':'form-control'}))
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']

class SearchForm(forms.Form):
    query = forms.CharField(label="Ключевое слово для поиска:", widget=forms.TextInput(attrs={'class':'form-control'}), max_length=30)
    