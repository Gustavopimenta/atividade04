from django.contrib import admin
from django.urls import path
from olamundo import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.hello_world, name='hello-world'),
]
