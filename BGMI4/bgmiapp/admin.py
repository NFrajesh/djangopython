from django.contrib import admin
from .models import Profile, solo_20_6_2021, solo_21_6_2021,duo_21_6_2021,squad_21_6_2021, withdraw

class SoloAdmin(admin.ModelAdmin):
    list_display = ('user','player1_pubg_id','player1_pubg_name','position','prize_amount')

class DuoAdmin(admin.ModelAdmin):
    list_display = ('user','player1_pubg_id','player1_pubg_name','player2_pubg_id','player2_pubg_name')

class SquadAdmin(admin.ModelAdmin):
    list_display = ('user','player1_pubg_id','player1_pubg_name','player2_pubg_id','player2_pubg_name','player3_pubg_id','player3_pubg_name','player4_pubg_id','player4_pubg_name')

class WithdrawAdmin(admin.ModelAdmin):
    list_display = ('user','withdraw_amount','UPI_ID')
admin.site.register(Profile)
admin.site.register(solo_21_6_2021,SoloAdmin)
admin.site.register(duo_21_6_2021,DuoAdmin)
admin.site.register(squad_21_6_2021,SquadAdmin)
admin.site.register(withdraw,WithdrawAdmin)
admin.site.register(solo_20_6_2021)

# Register your models here.
