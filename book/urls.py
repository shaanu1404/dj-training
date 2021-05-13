from django.urls import path

from . import views

urlpatterns = [
    path('', views.BookListView.as_view(), name="list"),
    path('create/', views.BookCreateView.as_view(), name="create"),
    path('<int:id>/', views.BookDetailView.as_view(), name="detail"),
    path('<int:pk>/update/', views.BookUpdateView.as_view(), name="update"),
    path('<int:pk>/delete/', views.BookDeleteView.as_view(), name="delete"),
]