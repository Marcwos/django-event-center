from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('verify-owners/', views.verify_owners, name='verify_owners'),  # Verificación del Administrador
]
