from django.views.generic import TemplateView

class HomePageView(TemplateView):
    template_name = 'ims/home.html'

class AboutPageView(TemplateView):
    template_name = 'ims/about.html'



