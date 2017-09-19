from django.contrib import admin
from app import models
# Register your models here.

class BBS_admin(admin.ModelAdmin):
    list_display = ('title','summary','auth','signature','view_count','create_d')
    list_filter = ('create_d',)#元组
    search_fields = ('title','auth__user__username')

    def signature(self,obj):
        return obj.auth.signature
    signature.short_description = 'person_QM'#把signature改成person_QM显示



admin.site.register(models.BBS,BBS_admin)
admin.site.register(models.Category)
admin.site.register(models.BBS_user)