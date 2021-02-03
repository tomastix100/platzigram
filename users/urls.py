"""Users URLs."""

# Django
from django.urls import path

# View
from users import views

# Posts
# Mucho ojo con este tipo de vistas, si llegamos a quitar de la url el profile/, todo se va a fk, porque lo que hace Django es mostrar las vistas que no estan protegidas, esta vista al ser de tipo generico no se le puede poner proteccion de tener una sesión activa para poderl mostrar
"""path(
    route='profile/<str:username>/',
    view=TemplateView.as_view(template_name='users/detail.html'),
    name='detail'
)"""

urlpatterns = [

    # Posts
    path(
        route='profile/<str:username>/',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # Management
    path(
        route='login/',
        view=views.login_view,
        name='login'
    ),
    path(
        route='logout/',
        view=views.logout_view,
        name='logout'
    ),
    path(
        route='signup/',
        view=views.signup,
        name='signup'
    ),
    path(
        route='me/profile/',
        view=views.update_profile,
        name='update'
    )

]