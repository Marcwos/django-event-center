
from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
from django.views import View
from usuarios.models import CustomUser  # Asegúrate de importar tu modelo de usuario personalizado

class ContactoView(View):
    def get(self, request):
        return render(request, 'contacto.html')

    def post(self, request):
        # Recoger datos del formulario
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        numero_pedido = request.POST.get('numero_pedido')
        mensaje = request.POST.get('mensaje')

        # Asegurarse de que se han recibido todos los datos necesarios
        if not all([nombre, correo, numero_pedido, mensaje]):
            return render(request, 'contacto.html', {'error': 'Por favor, completa todos los campos.'})

        # Obtener el correo del dueño con el rol de 'admin'
        try:
            dueño = CustomUser.objects.get(role='admin')  # Busca un usuario con el rol de 'admin'
            correo_dueño = dueño.email
        except CustomUser.DoesNotExist:
            return render(request, 'contacto.html', {'error': 'No se pudo encontrar el correo del dueño.'})

        # Crear el contenido del correo
        subject = 'Nuevo mensaje de contacto'
        body = (
            f"Nombre: {nombre}\n"
            f"Correo: {correo}\n"
            f"Número de Pedido: {numero_pedido}\n"
            f"Mensaje: {mensaje}"
        )

        # Enviar correo
        try:
            msg = EmailMultiAlternatives(
                subject,
                body,
                settings.EMAIL_HOST_USER,
                [correo_dueño]  # Envía el correo al dueño
            )
            msg.send()
            return render(request, 'contacto.html', {'success': 'Correo enviado correctamente'})
        except Exception as e:
            return render(request, 'contacto.html', {'error': f'Error al enviar el correo: {e}'})
