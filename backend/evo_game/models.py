from django.db import models

class Population(models.Model):
    name = models.CharField(max_length=200)
    size = models.IntegerField()

    def __str__(self):
        return self.name
    
