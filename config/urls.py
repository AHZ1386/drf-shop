
from django.contrib import admin
from django.urls import path
from API.views import test


urlpatterns = [
    path('admin/', admin.site.urls),
    path("Api/", test)
]
