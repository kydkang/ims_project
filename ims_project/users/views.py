from django.urls  import reverse_lazy 
from django.views import generic
from .forms import CustomUserCreationForm

class SignUp(generic.CreateView): 
    form_class = CustomUserCreationForm      # created in the previous chapter
    success_url = reverse_lazy('login')    ## the urls[[ ‘login’ ]] are not loaded when the file is imported, 
                                           ## so we have to use the lazy form of reverse to load them later when they’re available
    template_name = 'signup.html'        # created above 

