from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('send/', views.Send.as_view(), name='send'),
    path('signin/', views.signin, name='signin'),
]
