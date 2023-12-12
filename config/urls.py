
from django.contrib import admin
from django.urls import path
from API.views import UserProfileView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/<int:id>',UserProfileView.as_view(), )
]
