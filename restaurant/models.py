from __future__ import unicode_literals

from django.db import models

# Create your models here.

class FoodOrder(models.Model):
    category = models.CharField(max_length=50) 
    item = models.CharField(max_length=100) 
    price = models.CharField(max_length=20)

    def __str__(self):
        return '%s %s %s' % (self.category, self.item, self.price)