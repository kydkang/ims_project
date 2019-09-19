from django.contrib import admin
from django.urls import path, include 
from django.views.generic.base import TemplateView

urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('', include('ims.urls')),

    path('', TemplateView.as_view(template_name='home.html'), name='home'), 
    path('index/', include('ims.urls'), name='index_home'), 
    path('admin/',   admin.site.urls), 
    path('users/', include('users.urls')), 
    path('users/', include('django.contrib.auth.urls')), 

]