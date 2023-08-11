from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from accounts.forms import RegisterUserForm, UserEditForm, ProfileEditForm
from .models import Profile
from django.contrib import messages
# Create your views here.

def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is None:
            login(request, user)
            return redirect("main:home")
        else:
            messages.success(request, ("Имя пользовател и/или пароль были введены неправильно. Повторите попытку."))
            return redirect('main:add')
    else: 
        return render(request, 'authentication/login.html', {})
    
def logout_user(request):
    logout(request)
    messages.success(request, ("Вы вышли из аккаунта."))
    return redirect('main:home')

def register_user(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Вы вошли в аккаунт."))
            Profile.objects.create(user=user)
            return redirect('main:home')
    else: 
        form = RegisterUserForm()
    return render(request, 'authentication/register_user.html', {'form': form,})


@login_required
def edit(request):
    if request.method == "POST":
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile,
                                       data=request.POST,
                                       files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Учетная запись успешно обновлена.')
        else:
            messages.error(request, 'Произошла ошибка при обновлении учетной записи.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 
                  'account/edit.html', 
                  {'user_form':user_form,
                   'profile_form':profile_form})