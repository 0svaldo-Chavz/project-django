from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Project
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from django.contrib.auth.decorators import login_required
from .forms import ProjectForm
# from .helpers import auth

# Create your views here.


def main(request):
    if request.method == 'GET':
        return render(request, 'main.html')
    elif request.method == 'POST':
        print(request.POST)
        print(request.POST.get('btn-login-form'))
        # SignUp
        if 'btn-signup-form' in request.POST:
            # auth.signupUser(request)
            if request.POST['password1'] == request.POST['password2']:
                try:
                    # register user
                    user = User.objects.create_user(
                        username=request.POST['sign_username'], password=request.POST['password1'], email=request.POST['email'])
                    user.save()
                    login(request, user)
                    return redirect('home')
                except IntegrityError:
                    return render(request, 'main.html', {
                        'error': 'Username already exists'
                    })
        # Login
        elif 'btn-login-form' in request.POST:
            user = authenticate(
                request, username=request.POST['log_username'], password=request.POST['password'])

            if user is None:
                return render(request, 'main.html', {
                    'error': 'Username or password is incorrect'
                })
            else:
                login(request, user)
                return redirect('home')

    else:
        return render(request, 'main.html', {
            'error': 'No se obtuvo ninguna respuesta válida. Intente de nuevo.'
        })


@login_required
def home(request):
    projects = Project.objects.filter(
        user=request.user)
    return render(request, 'home.html', {
        'projects': projects
    })


@login_required
def signOut(request):
    logout(request)
    return redirect('main')


@login_required
def create_project(request):

    if request.method == 'GET':
        return render(request, 'create_project.html', {
            'form': ProjectForm
        })
    else:
        print(request.POST)
        try:
            form = ProjectForm(request.POST, request.FILES)
            print('Este es files: ', request.FILES)
            project = form.save(commit=False)
            project.user = request.user
            project.save()
            return redirect('home')
        except ValueError:
            return render(request, 'create_project.html', {
                'form': ProjectForm,
                'error': 'Please provide valide data'
            })
