from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from .views import home , about , register , profile


urlpatterns = [
    path('', home, name='home'),
    path('login/', LoginView.as_view( template_name='Login.html')),
    path('about/',about,name='about'),
path('logout/',LogoutView.as_view(template_name='logout.html'),name='logout'),
    path('register/',register,name='register'),
    path('profile/',profile,name='profile'),

]