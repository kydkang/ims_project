from django.db import models
from django.urls import reverse

class Department(models.Model):
    name = models.CharField(max_length=100, help_text='Enter department name')

    def __str__(self):
        return self.name

class Index(models.Model):  
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100,  help_text='Enter index name')
    data_one = models.IntegerField()
    data_two = models.DecimalField(max_digits=5, decimal_places=2)
    calculated_value = models.CharField(max_length=32, blank=True, )  # to make it not visible in admin, use  editable=False

    def calculate(self):
        return self.data_one + self.data_two

    def save(self, *args, **kwargs):
        self.calculated_value =  self.calculate() 
        super(Index, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('index_detail', args=[str(self.department.id), str(self.id)])
         # or  kwargs={'year': self.pub_date.year, 'slug': self.slug})