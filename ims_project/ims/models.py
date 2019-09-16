from django.db import models
# from decimal import Decimal 
import decimal

class Dname_Indexname(models.Model):
    name = models.CharField(max_length=100,  help_text='Enter index name')
    data_one = models.IntegerField()
    data_two = models.DecimalField(max_digits=5, decimal_places=2)
    calculated_value = models.CharField(max_length=32, blank=True, editable=False)

    def calculate(self):
        return self.data_one + self.data_two

    def save(self, *args, **kwargs):
        self.calculated_value =  self.calculate() 
        super(Dname_Indexname, self).save(*args, **kwargs)

    def __str__(self):
        return self.name
