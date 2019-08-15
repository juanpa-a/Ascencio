# django
from django.contrib import admin
from django.urls import path
# local
from ascencio.views.testing.test import hello


urlpatterns = [
    path('admin/', admin.site.urls),
    path()

]
