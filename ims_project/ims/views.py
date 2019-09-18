from django.views.generic import ListView
from .models import Department, Index

class HomePageView(ListView):
    model = Department                   ###  Or, queryset = Post.objects.all()
    template_name = 'ims/home.html'
    ###  [[ context_object_name = ‘posts’ ]]  instead of the defalut ‘object_list’

class IndexListView(ListView): 
    # model = Index
    template_name = 'ims/index_list.html' 
    def get_queryset(self):
        return Index.objects.filter(department=self.kwargs['did'])

    def get_context_data(self, **kwargs):
        context = super(IndexListView, self).get_context_data(**kwargs) # get the default context data
        context['did'] = self.kwargs['did'] # add extra field to the context
        return context

class IndexDetailView(ListView):
    model = Index 
    template_name = 'ims/index_detail.html'

    # somehow, the following function is need to pass the object to template....
    # you should use 'pk' in the url parameter to select the object for detailview
    def get_context_data(self, **kwargs):
        context = super(IndexDetailView, self).get_context_data(**kwargs)
        context['object'] = Index.objects.get(id=self.kwargs['pk'])
        return context



