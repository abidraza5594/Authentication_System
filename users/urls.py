from django.urls import path
from users import views
from django.contrib.auth import views as auth_view

urlpatterns = [
    path('login/',auth_view.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('logout/',auth_view.LogoutView.as_view(template_name='users/logout.html'),name='logout'),
    path('register/',views.register,name='register'),
    path('profile/',views.profile,name='profile'),
    path('editprofile<int:id>/',views.editprofile,name='editprofile')
]
