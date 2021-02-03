"""User forms."""

# Django
from django import forms

# Models
from django.contrib.auth.models import User
from users.models import Profile


class SignupForm(forms.Form):
    """Sign up form."""

    username = forms.CharField(min_length=4, max_length=50)

    password = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )
    password_confirmation = forms.CharField(
        max_length=70,
        widget=forms.PasswordInput()
    )

    first_name = forms.CharField(min_length=2, max_length=50)
    last_name = forms.CharField(min_length=2, max_length=50)

    email = forms.CharField(
        min_length=6,
        max_length=70,
        widget=forms.EmailInput()
    )

    # Siempre que gamos la validacion de un campo tenemos que 
    # regresar el campo
    def clean_username(self):
        """Username must be unique."""
        username = self.cleaned_data['username']
        # Lo que hace es buscar los usarios que tengan ese username,
        # devuelve un True o False gracias al metodo *.exists()*
        username_taken = User.objects.filter(username=username).exists()
        
        if username_taken:
            # Ya Django sube la excepción hasta el nivel del HTML
            raise forms.ValidationError('Username is already in use.')
        return username
    
    def clean(self):
        """Verify password confirmation match"""
        # Como no quremos sobreescribir el metodo clean el cual manda  
        # a llamar otras cosas, entonces  vamos a traer los datos que
        # ya nos traeria clean si no lo hubieramos sobre escrito y esto
        # se hace con el siguiente codigo
        data = super().clean() # Esta es una forma de llamar el metodo antes de ser sobreescrito
        password = data['password']
        password_confirmation = data['password_confirmation']

        if password != password_confirmation:
            raise forms.ValidationError('Passwords do not match.')

        return data
    
    def save(self):
        """Create user and profile."""
        data = self.cleaned_data
        # Como este metodo no nos sirve para nada por eso tenemos que sacarlo,
        # se saca ya que solo es con el proposito de tener una contraseña con
        # su respectiva confirmacion. el modelo User no tiene ese campo por eso
        # se lo saca con el metodo *pop*
        data.pop('password_confirmation')
        # Los asteriscos lo que hacen es enviar la estructura desvaratada
        user = User.objects.create_user(**data)
        profile = Profile(user=user)
        profile.save()


class ProfileForm(forms.Form):
    """Profile form."""

    website = forms.URLField(max_length=200, required=True)
    biography = forms.CharField(max_length=500, required=False)
    phone_number = forms.CharField(max_length=20, required=False)
    picture = forms.ImageField()
