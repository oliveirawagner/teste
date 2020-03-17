from django.db import models

class Pessoa(models.Model):

    name = models.CharField(max_length=60)
    email = models.EmailField(null=True, blank=True)
    active = models.BooleanField(default=True)


    def __str__(self):
        return self.name
    
