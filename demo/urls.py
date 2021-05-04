from django.contrib import admin
from django.urls import path

from products.views import give_response, add_value

urlpatterns = [
    path('', give_response),
    path('about/', add_value),
    path('admin/', admin.site.urls),
]
