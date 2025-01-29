from django.shortcuts import render,redirect
from django.shortcuts import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import todo

# Create your views here.
@login_required(login_url="/login")
def index(request):
    objs = todo.objects.all().values()
    context = {
        'objs': objs
    }
    if request.method == "POST":
        data = request.POST
        print(data)
        todo.objects.create(title=data['titlex'], description=data['descriptionx'], status=False)
        # obj = todo (title = data.get(titlex), description = data.get(descriptionx), status=False)
        # obj.save()
    # return HttpResponse("Hello, world.")
    print(request.GET.get('search'))
    if request.GET.get('search'):
        qryst = queryset.filter(title__icontains = request.GET.get('search'))
    return render(request, "index.html", context = context)

@login_required(login_url="/login")
def delItem(request,ID):
    todo.objects.get(id=ID).delete()
    return redirect("/")

@login_required(login_url="/login")
def upItem(request,ID):
    obj = todo.objects.get(id=ID)
    if request.method == "POST":
        data = request.POST
        obj.title = data.get('titlex')
        obj.description = data.get('descriptionx')
        obj.save()
    context = {
        'objs': obj
    }
    return render(request, "update.html", context)

@login_required(login_url="/login")
def toggleItem(request,ID):
    obj = todo.objects.get(id=ID)
    obj.status = not obj.status
    obj.save()
    print("That ran")
    return redirect("/")


def login_page(request):
    if request.method == "POST":
        data = request.POST
        username = data.get("username")
        password = data.get("password")
        print(f"Username entered: {username}")
        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            messages.error(request, "User does not exist! Register?")
            return redirect('/login/')
        user = authenticate(request,username = username, password = password)
        if user is None:
            messages.error(request, "Invalid password! trying brute force?")
            
        else:
            login(request, user)
            messages.info(request, "login successful")
            return redirect('/')
    return render(request, 'login.html')

@login_required(login_url="/login")
def logout_page(request):
    logout(request)
    return redirect('/login')

def register_page(request):
    if request.method == "POST":
        data = request.POST
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        username = data.get("username")
        password = data.get("password")

        user = User.objects.filter( username = username)
        if user.exists():
            messages.error(request, "User Already Exists!")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username,
        )

        user.set_password(password)
        user.save()
        messages.success(request, "Profile created successfully")
        return redirect('/register/')

    return render(request, 'register.html')