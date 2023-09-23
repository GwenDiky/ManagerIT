from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from accounts.forms import RegisterUserForm, UserEditForm, ProfileEditForm, ProfileDescriptionEditForm, ProfileEducationAndExperienceEditForm
from .models import Profile
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy 
from django.contrib.auth.views import PasswordChangeView
from django.contrib.messages.views import SuccessMessageMixin
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
        form = RegisterUserForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()

            user.profile.description = form.cleaned_data.get('description')
            user.profile.current_company = form.cleaned_data.get('company')
            user.profile.country = form.cleaned_data.get('country')
            user.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, ("Вы вошли в аккаунт."))
            #Profile.objects.create(user=user, job_title=job_title)
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
            return redirect('accounts:show_profile')
        else:
            messages.error(request, 'Произошла ошибка при обновлении учетной записи.')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    return render(request, 
                  'account/edit.html', 
                  {'user_form':user_form,
                   'profile_form':profile_form})


@login_required 
def edit_description(request):
    if request.method == "POST":
        description_form = ProfileDescriptionEditForm(instance=request.user.profile, data=request.POST)
        if description_form.is_valid():
            description_form.save()
            messages.success(request, 'Описание аккаунта успешно обновлено.')
            return redirect('accounts:show_profile')
        else:
            messages.error(request, 'Произошла ошибка при обновлении учетной записи.')

    else:
        description_form = ProfileDescriptionEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit_description.html',
                  {'description_form':description_form})

@login_required 
def edit_education_and_experience(request):
    if request.method == "POST":
        education_experience_form = ProfileEducationAndExperienceEditForm(instance=request.user.profile, data=request.POST)
        if education_experience_form.is_valid():
            education_experience_form.save()
            messages.success(request, 'Описание аккаунта успешно обновлено.')
            return redirect('accounts:show_profile')
        else:
            messages.error(request, 'Произошла ошибка при обновлении учетной записи.')

    else:
        education_experience_form = ProfileEducationAndExperienceEditForm(instance=request.user.profile)
    return render(request,
                  'account/edit_education_experience.html',
                  {'education_experience_form':education_experience_form})

def show_profile(request):
    profiles = Profile.objects.filter(user = request.user)
    return render(request, 'account/profile.html', {'profiles': profiles})

def all_profiles(request):
    all_profiles = Profile.objects.exclude(user = request.user)
    return render(request, 'account/all_profiles.html', {'all_profiles':all_profiles})

class ChangePasswordView(SuccessMessageMixin, PasswordChangeView):
    template_name = 'account/change_password.html'
    success_message = "Пароль успешно изменен"
    success_url = reverse_lazy('main:home')

"""class ShowProfilePageView(DetailView):
    model = Profile
    template_name = 'account/profile.html'

    def get_context_data(self, *args, **kwargs):
        users = Profile.objects.all()
        context = super(ShowProfilePageView, self).get_context_data(self, **kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context['page_user'] = page_user
        return context"""
    