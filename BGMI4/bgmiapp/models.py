from typing import Optional
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.utils.translation import gettext as _
class Profile(models.Model):
    user = models.OneToOneField(User,null=True, on_delete=models.CASCADE)
    pubg_id = models.PositiveIntegerField(null=True,blank=True)
    pubg_name = models.CharField(max_length=15,null=True,blank=True)
    phone_no = models.PositiveIntegerField(null=True,blank=True)
    balance = models.PositiveSmallIntegerField(default="0")
    form_submited=models.BooleanField(default=False)


    def __str__(self):
        return str(self.user)

    def create_user_profile(sender,instance,created,**kwargs):
        if created:
            Profile.objects.create(user=instance)
    post_save.connect(create_user_profile,sender=User)

class solo_21_6_2021(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    player1_pubg_id = models.PositiveIntegerField()
    player1_pubg_name = models.CharField(max_length=15)
    position = models.CharField(max_length=20,default="0")
    prize_amount = models.CharField(max_length=20,default="0")
     
    
    def __str__(self):
        return str(self.user)

class solo_20_6_2021(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    player1_pubg_id = models.PositiveIntegerField()
    player1_pubg_name = models.CharField(max_length=15)
    position = models.CharField(max_length=20,default="0")
    prize_amount = models.CharField(max_length=20,default="0")
     
    
    def __str__(self):
        return str(self.user)

class duo_21_6_2021(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    player1_pubg_id = models.PositiveIntegerField()
    player1_pubg_name = models.CharField(max_length=15)
    player2_pubg_id = models.PositiveIntegerField()
    player2_pubg_name = models.CharField(max_length=15)
     
    
    def __str__(self):
        return str(self.user)

class squad_21_6_2021(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    player1_pubg_id = models.PositiveIntegerField()
    player1_pubg_name = models.CharField(max_length=15)
    player2_pubg_id = models.PositiveIntegerField()
    player2_pubg_name = models.CharField(max_length=15)
    player3_pubg_id = models.PositiveIntegerField()
    player3_pubg_name = models.CharField(max_length=15)
    player4_pubg_id = models.PositiveIntegerField()
    player4_pubg_name = models.CharField(max_length=15)
     
    
    def __str__(self):
        return str(self.user)

class withdraw(models.Model):
    user = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    withdraw_amount=models.PositiveSmallIntegerField(verbose_name=_('Enter Amount'))
    UPI_ID=models.CharField(max_length=20)

    def __str__(self):
        return str(self.user)


# Create your models here.
  