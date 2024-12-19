from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django import forms

# Crear un formulario para manejar la verificación en el Admin
class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

    # Validar el código de verificación
    def clean(self):
        cleaned_data = super().clean()
        verification_code = cleaned_data.get('verification_code')
        is_verified = cleaned_data.get('is_verified')

        if is_verified and not verification_code:
            raise forms.ValidationError("No se puede verificar el usuario sin un código de verificación.")
        return cleaned_data

class CustomUserAdmin(UserAdmin):
    form = CustomUserAdminForm
    model = CustomUser
    list_display = ['username', 'email', 'role', 'is_verified']  # Mostrar estado de verificación
    list_filter = ['role', 'is_verified']  # Filtrar por estado de verificación

    fieldsets = UserAdmin.fieldsets + (
        ('Verification', {'fields': ('verification_code', 'is_verified')}),  # Agregar los campos
    )

    readonly_fields = ['verification_code']  # Hacer el campo de verificación de solo lectura

    # Acción para verificar manualmente al usuario
    actions = ['verify_user']

    def verify_user(self, request, queryset):
        for user in queryset:
            if user.verification_code:
                user.is_verified = True
                user.save()
                self.message_user(request, f"Usuario {user.username} verificado correctamente.")
            else:
                self.message_user(request, f"El usuario {user.username} no tiene código de verificación.", level='error')
    verify_user.short_description = "Verificar usuarios seleccionados"

admin.site.register(CustomUser, CustomUserAdmin)
