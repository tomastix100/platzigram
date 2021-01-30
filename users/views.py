"""Users views."""

# Django
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


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
