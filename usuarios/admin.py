from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from django import forms

class CustomUserAdminForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = '__all__'

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
    list_display = ['username', 'email', 'role', 'is_verified']
    list_filter = ['role', 'is_verified']

    fieldsets = UserAdmin.fieldsets + (
        ('Verification', {'fields': ('verification_code', 'is_verified')}),
    )

    readonly_fields = ['verification_code']

    actions = ['verify_user']

    def verify_user(self, request, queryset):
        for user in queryset:
            if user.verification_code:
                user.is_verified = True
                user.verification_code = None
                user.save()
                self.message_user(request, f"Usuario {user.username} verificado correctamente.")
            else:
                self.message_user(request, f"El usuario {user.username} no tiene código de verificación.", level='error')
    verify_user.short_description = "Verificar usuarios seleccionados"

admin.site.register(CustomUser, CustomUserAdmin)
