from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy 
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

    # somehow, the following function is needed to pass the object to template....
    # you should use 'pk' in the url parameter to select the object for detailview
    def get_context_data(self, **kwargs):
        context = super(IndexDetailView, self).get_context_data(**kwargs)
        context['object'] = Index.objects.get(id=self.kwargs['pk'])
        return context

from .form import IndexCreateForm 
from django.shortcuts import get_object_or_404 
class IndexCreateView(CreateView):
    # model = Index   # this line is moved to IndexCreateForm  
    form_class = IndexCreateForm
    template_name = 'ims/index_new.html'
    # fields = ['name', 'data_one', 'data_two']  # this line is moved to IndexCreateForm  

    def form_valid(self, form):
        dept = get_object_or_404(Department, id=self.kwargs['did'])   # get the dept object
        form.instance.department = dept 
        return super().form_valid(form) 


class IndexUpdateView(UpdateView):
    model = Index
    fields = ['data_one', 'data_two']
    template_name = 'ims/index_update.html'  

class IndexDeleteView(DeleteView): 
    model = Index
    template_name = 'ims/index_delete.html'

    def get_success_url(self):
        return reverse_lazy('index_list', args=[self.object.department.id]  ) 
        # Or, return reverse_lazy('index_list', kwargs={'did': self.object.department.id}  ) 


