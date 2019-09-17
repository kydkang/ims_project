from django.views.generic import ListView
from .models import Department

class HomePageView(ListView):
    model = Department                   ###  Or, queryset = Post.objects.all()
    template_name = 'ims/home.html'
    ###  [[ context_object_name = ‘posts’ ]]  instead of the defalut ‘object_list’


# class AboutPageView(TemplateView):
#     template_name = 'ims/about.html'



