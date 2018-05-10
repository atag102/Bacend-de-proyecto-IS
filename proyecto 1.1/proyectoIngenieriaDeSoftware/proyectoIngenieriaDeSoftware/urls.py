from django.contrib import admin
from django.urls import path
from django.conf.urls import url,include
from usuario.views import login

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",login.as_view(),name="login")
]
