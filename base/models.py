from django.db import models

# Create your models here.

class Room(models.Model):
    # host = 
    # topic = 
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank = True)
    # partcipants = 
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return self.name