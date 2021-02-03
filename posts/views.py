"""Posts views."""

# Django
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView

# Forms
from posts.forms import PostForm

# Models
from posts.models import Post

# class PostsFeedView(
#                   Login obligatorio para estar en esta vista,
#                   Vita generica para listar elementos
# ):
class PostsFeedView(LoginRequiredMixin, ListView):
    """Return all published posts."""

    # Template donde cargara toda la información
    template_name = 'posts/feed.html'
    # Modelo, ya que es una lista lo que hara sera 
    # consultar todos los posts.
    model = Post
    # Ordena la consulta de la mas reciente a la 
    # la mas antigua
    ordering = ('-created',)
    # Para mostrar en una paginacion de a dos elementos
    paginate_by = 30
    # Define el nombre del query en el contexto, eso 
    # quiere decir que de ahi se sacaran los datos
    context_object_name = 'posts'

class PostDetailView(LoginRequiredMixin, DetailView):
    """Return post detail."""

    template_name = 'posts/detail.html'
    queryset = Post.objects.all()
    context_object_name = 'post'

@login_required
def create_post(request):
    """Create new post view."""
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts:feed')

    else:
        form = PostForm()

    return render(
        request=request,
        template_name='posts/new.html',
        context={
            'form': form,
            'user': request.user,
            'profile': request.user.profile
        }
    )
