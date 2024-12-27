from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django import forms

class CustomUserAdminForm(forms.ModelForm):
    verification_code_input = forms.CharField(
        label="Código de Verificación",
        required=False,
        help_text="Ingresa el código de verificación enviado al correo del administrador."
    )

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'role', 'cedula']  # No incluir is_verified

    def clean(self):
        cleaned_data = super().clean()
        verification_code_input = cleaned_data.get('verification_code_input')

        # Validar que se ingresa el código de verificación
        if not verification_code_input:
            raise forms.ValidationError("Debes ingresar el código de verificación para verificar al usuario.")
        
        return cleaned_data

class CustomUserAdmin(UserAdmin):
    form = CustomUserAdminForm
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_verified']
    list_filter = ['role', 'is_verified']

    fieldsets = UserAdmin.fieldsets + (
        ('Verification', {'fields': ('verification_code_input',)}),  # Solo incluir el código
    )

    # Eliminar readonly_fields si no se necesita mostrar el código de verificación
    actions = ['verify_user']

    def save_model(self, request, obj, form, change):
        # Verificar el código de verificación al guardar
        verification_code_input = form.cleaned_data.get('verification_code_input')
        if verification_code_input == obj.verification_code:
            obj.is_verified = True  # Verificar automáticamente si el código es correcto
            obj.verification_code = None  # Limpiar el código de verificación
        else:
            self.message_user(request, f"El código de verificación ingresado para el usuario {obj.username} no es válido.", level='error')
        
        super().save_model(request, obj, form, change)  # Guardar el objeto

admin.site.register(CustomUser, CustomUserAdmin)
