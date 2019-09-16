from django.db import models

class Index(models.Model):
    name = models.CharField(max_length=100,  help_text='Enter field documentation', unique=True)

    def __str__(self):
        return self.name
