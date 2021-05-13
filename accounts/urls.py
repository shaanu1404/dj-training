from django.urls import path

from accounts.views import user_register, login_user, logout_view

urlpatterns = [
    path('register/', user_register, name="register"),
    path('login/', login_user, name="login"),
    path('logout/', logout_view, name="logout"),
]