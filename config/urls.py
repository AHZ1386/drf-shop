
from django.contrib import admin
from django.urls import path
from API.views import test,update_test,delete_test


urlpatterns = [
    path('admin/', admin.site.urls),
    path("user/", test),
    path('update-user/<int:id>/',update_test),
    path('delete-user/<int:id>/',delete_test)
]
