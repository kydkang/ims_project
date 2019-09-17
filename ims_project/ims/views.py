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
        return Index.objects.filter(department=self.kwargs['id'])

class IndexDetailView(ListView):
    model = Index 
    template_name = 'ims/index_detail.html'

    # somehow, the following function is need to pass the object to template....
    def get_context_data(self, **kwargs):
        context = super(IndexDetailView, self).get_context_data(**kwargs)
        context['object'] = Index.objects.get(id=self.kwargs['pk'])
        return context



