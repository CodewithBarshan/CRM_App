from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from .forms import SignupForm,AddRecordForm
from .models import Record
# Create your views here.

def home(request):
    records=Record.objects.all()
    #check to see if logging in
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        #Lets authenicate
        user = authenticate (username=username , password=password)
        if user is not None:
            login(request,user )
            messages.success(request,"You have been successfully logged in")
            return redirect('home')
        else:
            messages.error(request,'Invalid Credentials! Please try again.')
            return redirect('home')
    else:
        return render(request,'website/home.html',{'records':records})
    


def logout_user(request):
    logout(request)
    messages.success(request,"You have been loged out!")
    return redirect('home')

def regsiter_user(request):
    if request.method == 'POST' :
        form=SignupForm(request.POST)
        if form.is_valid():
            form.save()
            #authenticate and login
            username=form.cleaned_data['username']
            password=form.cleaned_data['password1']
            user = authenticate (username=username , password=password)
            login(request,user)
            messages.success(request,"You have been successfully registered !")
            return redirect('home')
    else:
        form=SignupForm()
        return render(request,'website/register.html',{'form':form})
    return render(request,'website/register.html',{'form':form})

def customer_record(request,pk):
    if request.user.is_authenticated:
        #look up the records
        customer_record=Record.objects.get(id=pk)
        return render(request,'website/record.html',{'customer_record':customer_record})
    else:
        messages.success(request,"You must be logged in to view that page")
        return redirect('home')

def delete_record(request,pk):
    if request.user.is_authenticated:
            delete_record=Record.objects.get(id=pk)
            delete_record.delete()
            messages.success(request,"Record Successfully deleted !")
            return redirect('home')
    else:
        messages.success(request,"You must be logged in to view that page")
        return redirect('home')
def add_record(request):
    form=AddRecordForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method=='POST':
            if form.is_valid():
                add_record=form.save()
                messages.success(request,"You have successfully added the record !")
                return redirect('home')
        return render(request,'website/add_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to view that page")  
        return redirect('home')  

def update_record(request,pk):
    if request.user.is_authenticated:
        current_record=Record.objects.get(id=pk)
        form=AddRecordForm(request.POST or None,instance=current_record)
        if form.is_valid():
            form.save()
            messages.success(request,"Record has been updated !")
            return redirect('home')
        return render(request,'website/update_record.html',{'form':form})
    else:
        messages.success(request,"You must be logged in to view that page")
        return redirect('home') 