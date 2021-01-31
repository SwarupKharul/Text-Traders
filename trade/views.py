from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from .Forms import BooksForm
from .models import Books
from django.utils import timezone

# Create your views here.

def home(request):
    return render(request, 'home.html')

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm()})
    else:
        # Create a new user
        if request.POST['password1'] == request.POST['password2']:
            try:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'], email=request.POST['email'])
                email = request.POST['email'].lower()
                r = User.objects.filter(email=email)
                if r.count():
                    return render(request, 'signupuser.html',
                                  {'error': 'Email already exists'})
                else:
                    user.save()
                    login(request, user)
                    return redirect('userhome')

            except IntegrityError:
                return render(request, 'signupuser.html',
                              {'error': 'This username has already been taken. Please choose a new Username'})
            except ValueError:
                return render(request, 'signupuser.html',
                              {'error': 'Please enter valid username'})
        else:
            # tell the user the password didn't match
            return render(request, 'signupuser.html', {'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html',
                          {'form': AuthenticationForm(), 'error': 'User password did not match'})
        else:
            login(request, user)
            return redirect('userhome')

def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

def userhome(request):
    return render(request, 'userhome.html')

def publishbook(request):
    if request.method == 'GET':
        return render(request, 'publishbook.html', {'form': BooksForm()})
    else:
        try:
            form = BooksForm(request.POST)
            newbook = form.save(commit=False)
            newbook.user = request.user
            newbook.save()
            return redirect('userhome')
        except ValueError:
            return render(request, 'publishbook.html',
                          {'form': BooksForm(), 'error': 'Wrong data put in. Try Again'})

def academic(request):
    books = Books.objects.filter(academic="academic")
    return render(request, 'academic.html', {'books': books})

def nonacademic(request):
    books = Books.objects.filter(academic="non-academic")
    return render(request, 'non-academic.html', {'books': books})