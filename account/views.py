from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, get_user_model, login
from django.contrib.auth import authenticate

User = get_user_model()


def signup_view(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check password
        if password == password2:
            # check name
            if User.objects.filter(name=name).exists():
                messages.error(request, 'name is already used')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'email is already used')
                    return redirect('signup')
                else:
                    user = User.objects.create_user(
                        name=name,
                        email=email,
                        password=password)
                    user.save()
                    messages.success(request, 'you are now sign up')
                    return redirect('login')
        else:
            messages.error(request, 'passwords do not match')

        return redirect('signup')
    else:
        return render(request, 'account/signup.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = authenticate(
            request,
            email=email,
            password=password
        )

        if user is not None:
            login(request, user)
            messages.success(request, 'You are now login')
            return redirect('index')
        else:
            messages.error(request, 'Email or Password are not correct ')
            return redirect('login')

    else:
        return render(request, 'account/login.html')


def logout_view(request):
    logout(request)
    messages.success(request, 'logged out ')

    return redirect('index')


def password_change(request):
    return render(request, 'account/password_change.html')


def password_change_done(request):
    return render(request, 'account/password_change_done.html')


def password_change_reset(request):
    return render(request, 'account/password_change_reset.html')


def password_change_reset_done(request):
    return render(request, 'account/password_change_reset_done.html')


def password_reset_conrifm(request):
    return render(request, 'account/password_reset_conrifm.html')


def reset_done(request):
    return render(request, 'account/reset_done.html')
