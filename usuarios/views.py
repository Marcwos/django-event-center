import random
from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login, logout as auth_logout, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.views import View
from .forms import CustomUserCreationForm
from .models import CustomUser


def signup(request):  
    if request.method == 'GET':  
        return render(request, "usuarios/signup.html", {  
            'form': CustomUserCreationForm()  
        })  
    else:  
        if request.POST['password1'] == request.POST['password2']:  
            form = CustomUserCreationForm(request.POST)
            if form.is_valid():
                try:
                    user = form.save(commit=False)

                    # Verificar si el checkbutton "Dueño" está marcado
                    is_owner = request.POST.get('is_owner')  # Obtiene el valor del checkbox
                    if is_owner:  # Si el usuario elige ser dueño
                        user.is_staff = True
                        user.is_verified = False
                        user.verification_code = str(random.randint(100000, 999999))
                        user.save()

                        # Enviar correo de verificación al administrador
                        send_mail(
                            'Verificación de Registro - Dueño',
                            f'Nuevo registro pendiente: {user.username}. Código: {user.verification_code}',
                            settings.EMAIL_HOST_USER,
                            [settings.DEFAULT_ADMIN_EMAIL],  # Correo del administrador
                            fail_silently=False,
                        )

                        messages.info(request, "Registro exitoso. Pendiente de verificación del Administrador.")
                        return redirect('login')

                    # Si es cliente, completar registro directamente
                    user.is_verified = True
                    user.is_staff = False
                    user.save()
                    auth_login(request, user)
                    messages.success(request, "Usuario registrado correctamente.")
                    return redirect('home')

                except Exception as e:
                    print(e)
                    return render(request, "usuarios/signup.html", {  
                        "form": form,   
                        "error": "Error al registrar el usuario. Intenta de nuevo."  
                    })
            else:
                return render(request, "usuarios/signup.html", {  
                    "form": form,   
                    "error": "Formulario inválido. Revisa los datos ingresados."  
                })
        else:  
            return render(request, "usuarios/signup.html", {  
                "form": CustomUserCreationForm(),   
                "error": "Las contraseñas no coinciden."  
            })


def login(request):
    if request.method == 'GET':
        return render(request, 'usuarios/login.html', {
            'form': AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password']
        )
        if user is None:
            return render(request, 'usuarios/login.html', {
                'form': AuthenticationForm(),
                'error': 'Username o contraseña incorrectos.'
            })
        elif not user.is_verified:
            return render(request, 'usuarios/login.html', {
                'form': AuthenticationForm(),
                'error': 'Tu cuenta aún no ha sido verificada por el Administrador.'
            })
        else:
            auth_login(request, user)
            return redirect('home')


@login_required
def logout(request):
    auth_logout(request)
    return redirect('login')


# Verificación del Administrador
@login_required
def verify_owners(request):
    if not request.user.is_superuser:
        messages.error(request, "No tienes permisos para acceder a esta página.")
        return redirect('home')

    pending_owners = CustomUser.objects.filter(is_verified=False, is_staff=True)

    if request.method == 'POST':
        user_id = request.POST.get('user_id')
        verification_code = request.POST.get('verification_code')

        user = CustomUser.objects.filter(id=user_id, verification_code=verification_code).first()
        if user:
            user.is_verified = True
            user.verification_code = None
            user.save()
            messages.success(request, f"Usuario {user.username} verificado exitosamente.")
        else:
            messages.error(request, "Código incorrecto. Verificación fallida.")

    return render(request, 'usuarios/verify_owners.html', {'owners': pending_owners})


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
