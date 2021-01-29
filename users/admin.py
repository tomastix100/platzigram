"""User admin classes."""

# Django
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib import admin

# Models
from django.contrib.auth.models import User
from users.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile admin."""

    list_display = ('pk', 'user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk', 'user',)
    list_editable = ('phone_number', 'website', 'picture')

    search_fields = (
        'user__email',
        'user__username',
        'user__first_name',
        'user__last_name',
        'phone_number'
    )

    list_filter = (
        'user__is_active',
        'user__is_staff',
        'created',
        'modified',
    )
    # Cuando colocamos los fields dentro de una sola tupla, estos se van a visualizar
    # en columna, si los encerramos en dos, estos se veran horizontales
    fieldsets = (
        ('Profile', { # Este seria el tituo de la categoria
            'fields': (('user', 'picture'),), 
        }),
        ('Extra info', { # Este seria el tituo de la categoria
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Metadata', { # Este seria el tituo de la categoria
            'fields': (('created', 'modified'),),
        })
    )
    # Estas son variables que se van a poder ver en la categoria Metadata
    # pero no se van apoder editar, si no colocaramos estas dentro de la 
    # variable readonly_fields nos daria un error, ya que estamos diciendo 
    # que se puede editar campos que son automaticps, cada que se crea un registro,
    # por tal razon se deben bloquear su edición.

    readonly_fields = ('created', 'modified',)

class ProfileInline(admin.StackedInline):
    """Profile in-line admin for users."""

    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'


class UserAdmin(BaseUserAdmin):
    """Add profile admin to base user admin."""

    inlines = (ProfileInline,)
    # Aca van los campos que queremos que nos muestre
    list_display = (
        'username',
        'email',
        'first_name',
        'last_name',
        'is_active',
        'is_staff'
    )


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
