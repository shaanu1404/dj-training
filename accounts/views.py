from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout

from .forms import UserCreateForm, LoginForm


def user_register(request):
    form = UserCreateForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect(reverse('all_products'))

    context = {
        "form": form
    }
    return render(request, 'accounts/register.html', context)


def login_user(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST":
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user=user)
                return redirect(reverse('all_products'))
            else:
                print("Invalid user")

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def logout_view(request):
    if request.method == "POST":
        logout(request)
    return redirect(reverse('all_products'))