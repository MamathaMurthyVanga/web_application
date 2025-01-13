from django.shortcuts import render, redirect
from .models import App
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .serializers import AppSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.

def admin(request):
    if request.method =='POST':
        

        app_icon = request.FILES.get('app_icon')
        app_name = request.POST.get('app_name')
        app_link = request.POST.get('app_link')
        app_category = request.POST.get('app_category')
        sub_category = request.POST.get('sub_category')
        points = request.POST.get('points')

        fb = App(app_icon=app_icon, app_name=app_name,app_link=app_link,app_category=app_category,sub_category=sub_category,points=points)
        fb.save()
        
        return render(request, 'admin.html')


    a = App.objects.all()
    return render(request, 'admin.html')

def signin(request):
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
                messages.info(request, 'username already exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email already exists')
                return redirect('register')
            else:
                user = User.objects.create_user(
                username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, 'registration successfullw')
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

        if user is not None:
            auth.login(request, user)
            # messages.info(request, 'login successful')
            return render(request, 'admin.html')
        else:
            messages.info(request, 'Invalid Credentials')
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')


@api_view(['GET'])
def dataget(request):
    apps_data = App.objects.all()  # Fetch all App objects
    serializer = AppSerializer(apps_data, many=True)  # Serialize the data
    return Response(serializer.data)

@api_view(['DELETE'])
def deletedata(request, id):
    try:
        # Retrieve the object by id
        obj = App.objects.get(id=id)
        # Delete the object
        obj.delete()
        return Response({"message": "Data deleted successfully"}, )
    except App.DoesNotExist:
        # Handle the case where the object doesn't exist
        return Response({"error": "Data not found"})
    

