"""Users views."""

# Django
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import views as auth_views
from django.urls import reverse, reverse_lazy
from django.views.generic import DetailView, FormView, UpdateView

# Models
from django.contrib.auth.models import User
from posts.models import Post
from users.models import Profile

# Forms
from users.forms import SignupForm

# LoginRequiredMixin: lo que hace es colocar restriccion de 
# Login a la vista generica, solo sirve para estas vistas
class UserDetailView(LoginRequiredMixin, DetailView):
    """User detail view."""

    template_name = 'users/detail.html'
    # Campo de texto unico
    slug_field = 'username'
    # Como se llama el parametro que llega en la url
    slug_url_kwarg = 'username'
    # Apartir de que conjunto de datos va a traer los datos
    queryset = User.objects.all()
    context_object_name = 'user'
    # Metodo para agregar data al contexto
    def get_context_data(self, **kwargs):
        """Add user's posts to context."""
        # Traemos el contexto que ubiera traido si no hubieramos sobrescrito el metodo
        context = super().get_context_data(**kwargs)
        # Se encarga de ser el queryset del object segun los valores que nosotros le pasemos
        user = self.get_object()
        context['posts'] = Post.objects.filter(user=user).order_by('-created')
        return context

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    """Update profile view."""

    template_name = 'users/update_profile.html'
    model = Profile
    fields = ['website', 'biography', 'phone_number', 'picture']

    # Regresa el peril del usuario
    def get_object(self):
        """Return user's profile."""
        return self.request.user.profile
    """
    self.object : Este es el objeto que se recata del metodo 
    *def get_object(self):*, siendo este objeto el profile
    """
    def get_success_url(self):
        """Return to user's profile."""
        username = self.object.user.username
        return reverse('users:detail', kwargs={'username': username})

class LoginView(auth_views.LoginView):
    """Login view."""

    template_name = 'users/login.html'

class LogoutView(LoginRequiredMixin, auth_views.LogoutView):
    """Logout view."""
    # Como solo es cuestion de salir, no 
    template_name = 'users/logged_out.html'

class SignupView(FormView):
    """Users sign up view."""

    template_name = 'users/signup.html'
    form_class = SignupForm
    success_url = reverse_lazy('users:login')

    # SIEMPRE HAY QUE SOBREESCRIBIR ESTE METODO, PARA PODER 
    # CREAR LOS NUEVOS REGISTROS, SI ESTE NO SE SOBREESCRIBE
    # LO UNO QUE HARA SERA REIDRECCIONAR A LA URL QUE SE ENCUENTRE
    # REGISTRADA EN LA VARIABLE *success_url* 
    def form_valid(self, form):
        """Save form data."""
        form.save()
        # ESTO ES UNA LLAMADA AL METODO ORIGINAL, QUE LO QUE HACE
        # ES REDIRECCIONAR A LA URL EN LA QUE ESTE EN LA VARIABLE 
        # *success_url* 
        return super().form_valid(form)

"""
@login_required
def logout_view(request):
    # Logout a user
    logout(request)
    return redirect('users:login')

def login_view(request):
    # Login view
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('posts:feed')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid username and password'})

    return render(request, 'users/login.html')

def signup(request):
    # Sign up view
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('users:login')
    else:
        form = SignupForm()

    return render(
        request=request,
        template_name='users/signup.html',
        context={'form': form}
    )

@login_required
def update_profile(request):
    # Update a user's profile view
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
            # Froma cuando necesitamos enviar parametros en un redireccionamiento
            # con la función redirec
            url = reverse('users:detail', kwargs={'username': request.user.username})
            return redirect(url)

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
"""
