from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from admin.models import App
from user.models import MyApp
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.



def index(request):
    return render(request, 'index.html')


def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        

        if password1 == password2:

            if User.objects.filter(username=username).exists():
                messages.info(request, 'username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already taken')
                return redirect('register')
            else:
                user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'registration successful')
                return redirect('register')
        else:
            messages.info(request, 'password not matching')
            return redirect('register')

        
        

    else:
        return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        print(user, '999999999')

        if user is not None:
            auth.login(request, user)
            messages.info(request, 'login successful')
            return redirect('home')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'login.html')

def home(request):
    if request.user.is_authenticated:
        apps = App.objects.all()
        return render(request, 'home.html', {'apps': apps})
    else:
        return redirect('/')

def logout(request):
    auth.logout(request)
    return redirect('/')

@login_required
def app(request, id):
    if request.method == 'POST':
        
        app = App.objects.get(id=id)

        img = request.POST.get('img')
        app_name = request.POST.get('app_name')
        points = request.POST.get('points')

        myapp = MyApp(app_name=app_name, points=points, img=img)
        myapp.save()

        return render(request, 'app.html', {'app': app, 'img': img})
    app = App.objects.get(id=id)
    return render(request, 'app.html', {'app': app})

@login_required
def points(request):

    total_apps = [p for p in MyApp.objects.all()]

    total_points = 0

    app_points = []
    app_names = []
    for p in total_apps:
        total_points = total_points + p.points
        app_points.append(p.points)
        app_names.append(p.app_name)
    return render(request, 'points.html', {'total_points': total_points, 'app_points': app_points, 'app_names': app_names})

@login_required
def task(request):

    total_apps = [p for p in MyApp.objects.all()]
    app_names = []

    for p in total_apps:
        app_names.append(p.app_name)
    
    return render(request, 'task.html', {'app_names': app_names})

@login_required
def profile(request):
    return render(request, 'profile.html')


@login_required
def user(request):
    try:
        # Retrieve the data from MyApp model
        data = MyApp.objects.all()  # Adjust the fields you want
        return render(request, 'profile.html', {'data': data})
    except MyApp.DoesNotExist:
        return render(request, 'profile.html', {'message': 'No data found.'})



    
