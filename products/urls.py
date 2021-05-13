from django.urls import path

from .views import (
    all_products_view,
    single_product_view,
    create_new_product,
    edit_product,
    delete_product,
    contact_form_view,
)

urlpatterns = [
    path('', all_products_view, name='all_products'),
    path('create/', create_new_product, name='create_new_product'),
    path('<int:id>/', single_product_view,
         name='get_single_product'),
    path('<int:id>/edit/', edit_product, name='update_product'),
    path('<int:id>/delete/', delete_product,
         name='delete_product'),
]


# localhost:8000/  -- READ -- GET
# localhost:8000/create  -- CREATE -- POST
# localhost:8000/ID  -- READ -- GET
# localhost:8000/ID/edit  -- EDIT -- PUT/PATCH
# localhost:8000/ID/delete  -- DELETE -- DELETE
