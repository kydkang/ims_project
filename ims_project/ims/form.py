from django.forms import ModelForm
from .models import Index

class IndexCreateForm(ModelForm):
    class Meta:
        model=Index
        fields = ('name', 'data_one', 'data_two')