from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from django.forms.widgets import PasswordInput
from .models import Profile, solo_21_6_2021,duo_21_6_2021,squad_21_6_2021, withdraw

class RegisterForm(UserCreationForm):
    email=forms.EmailField(required=True,help_text=False)
    username=forms.CharField(help_text=False)
    password1=forms.CharField(help_text=False,widget=PasswordInput,label='password')
    password2=forms.CharField(help_text=False,widget=PasswordInput,label='confirm password')
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
    
    def save(self,commit=True):
        user = super(RegisterForm,self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
class UpdateProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('pubg_id', 'pubg_name', 'phone_no')
class SoloForm(forms.ModelForm):
    class Meta():
        model = solo_21_6_2021
        fields=['player1_pubg_id','player1_pubg_name']

class DuoForm(forms.ModelForm):
    class Meta():
        model = duo_21_6_2021
        fields=['player1_pubg_id','player1_pubg_name','player2_pubg_id','player2_pubg_name']

class SquadForm(forms.ModelForm):
    class Meta():
        model = squad_21_6_2021
        fields=['player1_pubg_id','player1_pubg_name','player2_pubg_id','player2_pubg_name','player3_pubg_id','player3_pubg_name','player4_pubg_id','player4_pubg_name']

class WithdrawForm(forms.ModelForm):
    class Meta():
        model = withdraw
        fields=['withdraw_amount','UPI_ID']


