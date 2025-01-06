
import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views import View
from .forms import CustomUserCreationForm
from .models import CustomUser
import random
from django.template import loader,Context
def signup(request):
    if request.method == 'GET':
        return render(request, "usuarios/signup.html", {'form': CustomUserCreationForm()})
    else:
        if request.POST['password1'] == request.POST['password2']:
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                try:
                    user = form.save(commit=False)
                    is_owner = request.POST.get('is_owner')
                    if is_owner:
                        user.role = 'admin'
                        user.is_staff = True
                        user.is_verified = False
                        user.verification_code = str(random.randint(100000, 999999))
                        user.save()
                        print("Enviando correo de verificación...")  # Verifica si este mensaje aparece en los logs
                        send_mail(
                        'Verificación de Registro - Dueño',
                        f'Nuevo registro pendiente: {user.username}. Código: {user.verification_code}',
                        settings.EMAIL_HOST_USER,
                        [settings.DEFAULT_ADMIN_EMAIL],
                        fail_silently=False,
                        )
                        messages.info(request, "Registro exitoso. Pendiente de verificación del Administrador.")
                        return redirect('login')


                    # Para usuarios normales
                    user.is_verified = True
                    user.is_staff = False
                    user.save()
                    auth_login(request, user)
                    messages.success(request, "Usuario registrado correctamente.")
                    return redirect('home')
                except Exception as e:
                    # Agrega un mensaje de error más detallado
                    print(f"Error al registrar el usuario: {e}")
                    return render(request, "usuarios/signup.html", {"form": form, "error": "Error al registrar el usuario."})
            else:
                return render(request, "usuarios/signup.html", {"form": form, "error": "Formulario inválido."})
        else:
            return render(request, "usuarios/signup.html", {"form": CustomUserCreationForm(), "error": "Las contraseñas no coinciden."})
        
def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'usuarios/login.html', {'form': AuthenticationForm(), 'error': 'Username o contraseña incorrectos.'})
        elif not user.is_verified:
            return render(request, 'usuarios/login.html', {'form': AuthenticationForm(), 'error': 'Tu cuenta aún no ha sido verificada.'})
        else:
            auth_login(request, user)
            return redirect('home')

@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


class Send(View):
    def get(self, request):
        return render(request, 'usuarios/send.html')

    def post(self, request):
        email = request.session.get('user_email')
        if email:
            template = get_template('usuarios/email-order-success.html')
            content = template.render({'email': email})
            msg = EmailMultiAlternatives(
                'Gracias por tu compra',
                'Hola, te enviamos un correo con tu factura',
                settings.EMAIL_HOST_USER,
                [email]
            )
            msg.attach_alternative(content, 'text/html')
            msg.send()
            return render(request, 'usuarios/send.html', {'success': 'Correo enviado correctamente'})
        else:
            return render(request, 'usuarios/send.html', {'error': 'No se pudo encontrar el correo del usuario'})

def signin(request):
    return render(request, "usuarios/login.html")
