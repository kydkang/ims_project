from django.forms import ModelForm
from .models import Index, IndexData  

class IndexCreateForm(ModelForm):
    class Meta:
        model=Index
        fields = ('name', 'data_one', 'data_two')

class IndexDataCreateForm(ModelForm):
    class Meta:
        model=IndexData
        fields = ('date', 'data_one', 'data_two')  
