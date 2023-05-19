from django.contrib import admin
from .models import DashModel, UserModel


# Register your models here.
admin.site.register(DashModel)
admin.site.register(UserModel)