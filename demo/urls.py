from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from products.views import (
    all_products_view,
    single_product_view,
    create_new_product,
    edit_product,
    delete_product,
    contact_form_view,
    )

urlpatterns = [
    path('', all_products_view, name='all_products'),    # localhost:8000/
    path('contact/', contact_form_view, name='contact'),    # localhost:8000/
    # localhost:8000/create
    path('create/', create_new_product, name='create_new_product'),
    path('<int:id>/', single_product_view,
         name='get_single_product'),  # localhost:8000/1
    # localhost:8000/1/edit
    path('<int:id>/edit/', edit_product, name='update_product'),
    path('<int:id>/delete/', delete_product,
         name='delete_product'),  # localhost:8000/1/delete
    path('admin/', admin.site.urls),
]


# localhost:8000/  -- READ -- GET
# localhost:8000/create  -- CREATE -- POST
# localhost:8000/ID  -- READ -- GET
# localhost:8000/ID/edit  -- EDIT -- PUT/PATCH
# localhost:8000/ID/delete  -- DELETE -- DELETE

urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)