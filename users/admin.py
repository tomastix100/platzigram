"""User admin classes."""

# Django
from django.contrib import admin

# Models
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    # Al darle click me lleva a la edicion
    list_display_links = ('pk', 'user',)
    # No pueden haver los mismos valores en la lista anterior y en esta siguiente
    # Me permite ditar ahi mismo el campo
    list_editable = ('phone_number', 'website', 'picture')

    # Para poder buscar en la barra de busqueda
    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )
    
    # Colocar filtros para busqueda
    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
