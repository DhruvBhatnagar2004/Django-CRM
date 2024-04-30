from django.shortcuts import render, redirect
from django.http import  HttpResponse
from .forms import createuserform, loginform, createrecord, updaterecord

from django.contrib.auth import authenticate
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from .models import record

from django.contrib import messages
# Create your views here.
def home(request):
    return render(request, 'myapp/index.html')
    
# register
def register(request):
    form=createuserform()
    if request.method == "POST":
        form = createuserform(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('login')
            
            
    context={'form':form}
    return render(request, 'myapp/register.html',context)  

# loginform
def login(request):
    form=loginform()
    
    if request.method =='POST':
        
        form=loginform(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')
            
            user=authenticate(request, username=username, password=password)
            
            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')
    
    context={'form2':form}
    
    return render(request, 'myapp/login.html',context=context)  

# dashboard

@login_required(login_url='login')  # restricting access to logged in users only
def dashboard(request):
    
    records=record.objects.all()
    context={'records':records}
    return render(request, 'myapp/dashboard.html', context=context)

# create record
@login_required(login_url='login')
def create(request):

    form = createrecord()

    if request.method == "POST":

        form = createrecord(request.POST)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was created!")

            return redirect("dashboard")

    context = {'form3': form}

    return render(request, 'myapp/create.html', context=context)

# - Update a record 

@login_required(login_url='login')
def update(request, pk):

    uprecord = record.objects.get(id=pk)

    form = updaterecord(instance=uprecord)

    if request.method == 'POST':

        form = updaterecord(request.POST, instance=uprecord)

        if form.is_valid():

            form.save()

            messages.success(request, "Your record was updated!")

            return redirect("dashboard")
        
    context = {'form':form}

    return render(request, 'myapp/update.html', context=context)

# - Read / View a record
@login_required(login_url='login')
def onerecord(request, pk):

    all_records = record.objects.get(id=pk)

    context = {'record':all_records}

    return render(request, 'myapp/view.html', context=context)


# - Delete a record
@login_required(login_url='login')
def delete(request, pk):

    delrecord = record.objects.get(id=pk)

    delrecord.delete()

    messages.success(request, "Your record was deleted!")

    return redirect("dashboard")

# logout
def logout(request):
    auth.logout(request)
    messages.success(request, "Logout Successful!")
    return redirect('login')   
