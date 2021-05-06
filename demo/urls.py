from django.contrib import admin
from django.urls import path

from products.views import all_products_view, single_product_view, create_new_product, edit_product, delete_product

urlpatterns = [
    path('', all_products_view),    # localhost:8000/
    path('create/', create_new_product),  # localhost:8000/create
    path('<int:id>/', single_product_view),  # localhost:8000/1
    path('<int:id>/edit/', edit_product),  # localhost:8000/1/edit
    path('<int:id>/delete/', delete_product),  # localhost:8000/1/delete
    path('admin/', admin.site.urls),
]


# localhost:8000/  -- READ -- GET
# localhost:8000/create  -- CREATE -- POST
# localhost:8000/ID  -- READ -- GET
# localhost:8000/ID/edit  -- EDIT -- PUT/PATCH
# localhost:8000/ID/delete  -- DELETE -- DELETE
