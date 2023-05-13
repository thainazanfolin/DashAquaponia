from django.contrib import admin
from django.urls import path, include

app_name = 'DashAquaponia'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('DashAquaponia.urls')),
]