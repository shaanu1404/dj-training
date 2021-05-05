from django.contrib import admin
from django.urls import path

from products.views import all_products_view, single_product_view

urlpatterns = [
    path('', all_products_view),    # localhost:8000/
    path('<int:id>/', single_product_view), # localhost:8000/1
    path('admin/', admin.site.urls),
]
