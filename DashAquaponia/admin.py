from django.contrib import admin
from .models import DashModel, User


# Register your models here.
admin.site.register(DashModel)
admin.site.register(User)