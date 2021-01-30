"""Users views."""

# Django
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# Exception
from django.db.utils import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile

# Forms
from users.forms import ProfileForm

@login_required
def update_profile(request):
    """Update a user's profile view."""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.website = data['website']
            profile.phone_number = data['phone_number']
            profile.biography = data['biography']
            profile.picture = data['picture']
            profile.save()

            return redirect('update_profile')

    else:
        form = ProfileForm()

    return render(
        request=request,
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
        }
    )


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        # Verificar las credenciales que se le estan pasando pormedio del metodo POST
        user = authenticate(request, username=username, password=password)
        if user:
            # Crea una sesión para el usuario
            login(request, user)
            # Despues de crear una sesión lo que hace es redirigir al usuario a una vista cuya URL se llama *feed*.
            return redirect('feed')
        else:
            # En caso de que las credenciales de usario no sean correptas lo que hara sera llamar a la vista login.html, para enviarle junto con ella un mensaje de error, este es personalizable. 
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})
    # Cuando se llame a esta direccioó se retornara la vista login.html
    return render(request, 'users/login.html')

@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')

def signup(request):
    """Sign up view."""
    if request.method == 'POST':
        # Capturamos los parametros que llegan en el request
        username = request.POST['username']
        passwd = request.POST['passwd']
        passwd_confirmation = request.POST['passwd_confirmation']

        if passwd != passwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'Password confirmation does not match'})

        try:
            # creamos el usuario, se coloca en una excepción ya que si el usuario ya existe lo que hace es saltar un error de Usuario existente
            user = User.objects.create_user(username=username, password=passwd)
        except IntegrityError:
            return render(request, 'users/signup.html', {'error': 'Username is already in user'})

        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save()

        return redirect('login')

    return render(request, 'users/signup.html')
