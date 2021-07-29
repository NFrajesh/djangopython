
from bgmiapp.models import *
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import RegisterForm,UpdateProfileForm,SoloForm,DuoForm,SquadForm,WithdrawForm
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView,UpdateView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect, request
 

def homeview(request):
    return render(request,'bgmiapp/home.html')



def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
           user= form.save()
           login(request,user)
           messages.success(request,"Registration success.")
           return HttpResponseRedirect(reverse_lazy('home'))
        else:
            messages.error(request,"Registeration Unsuccessful. Invalid Information")
    form=RegisterForm()
    return render(request,'bgmiapp/register.html',{'form':form})

def login_view(request):
    if request.method =="POST":
        form= AuthenticationForm(request,data=request.POST)
        if form.is_valid():
            username=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.info(request,f'you are now logged in as {username}')
                return HttpResponseRedirect(reverse_lazy('home'))
            else:
                messages.error(request,'Invalid Username and Password')
        else:
            messages.error(request,'Invalid Username and Password')
    form=AuthenticationForm()
    return render(request,'bgmiapp/login.html',{'form':form})


class ShowProfilePageView(DetailView):
    template_name = 'bgmiapp/show_profile.html'
    
    def get_object(self):
        return self.request.user.profile

class UpdateProfilePageView(SuccessMessageMixin,UpdateView):
    fields = ('pubg_id', 'pubg_name', 'phone_no')
    template_name='bgmiapp/update_profile.html'
    success_message = "Profile Updated Successfully"
    success_url= reverse_lazy('show_profile')
    

    def get_object(self):
        return self.request.user.profile



def solo(request):
    formsolo = SoloForm()
    if request.method=="POST":
        user=request.user.profile
        formsolo=SoloForm(request.POST)
        if formsolo.is_valid():
            f = formsolo.save(commit=False)
            f.user = request.user.profile
            if not user.form_submited:
                user.form_submited = True
                user.save()
                f.save()
                messages.success(request,"succesfully joined.")

                return redirect('home')
            else:
                messages.error(request,"You are already Joined in this match,please checkout the upcoming matches in Mymatches")
                return redirect('home')
        else:
            messages.error(request,"please fill the Form correctly")

    return render(request, 'bgmiapp/solo.html',{'formsolo':formsolo})

def duo(request):
    formduo = DuoForm()
    if request.method=="POST":
        formduo=DuoForm(request.POST)
        if formduo.is_valid():
            f = formduo.save(commit=False)
            f.user = request.user.profile

            f.save()
            messages.success(request,"successfully joined")
            return redirect('home')
        else:
            messages.ERROR(request,"please fill the Form correctly")
            

    return render(request, 'bgmiapp/duo.html',{'formduo':formduo})

def squad(request):
    formsquad = SquadForm()
    if request.method=="POST":
        formsquad=SquadForm(request.POST)
        if formsquad.is_valid():
            f = formsquad.save(commit=False)
            f.user = request.user.profile
            f.save()
            messages.success(request,"successfully joined")
            return redirect('home')
        else:
            messages.ERROR(request,"please fill the Form correctly")

    return render(request, 'bgmiapp/squad.html',{'formsquad':formsquad})
    
def Result(request):
    return render(request,'bgmiapp/result.html')

class ShowBalanceView(DetailView):
    template_name = 'bgmiapp/balance.html'
    
    def get_object(self):
        return self.request.user.profile

def WithdrawView(request):
    form=WithdrawForm()
    if request.method == "POST":
        form=WithdrawForm(request.POST)
        if form.is_valid():
            f=form.save(commit=False)
            f.user=request.user.profile
            f.save()
            messages.success(request,"Withdraw Requested")
            return redirect('home')
        else:
            messages.ERROR(request,'Invalid Informations')
    return render(request,'bgmiapp/withdraw.html',{'form':form})



def Solomatchresult(request):
    solomatchresult = solo_20_6_2021.objects.all()
    return render(request,'bgmiapp/solomatchresult.html',{'solomatchresult':solomatchresult})
