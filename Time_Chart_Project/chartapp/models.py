from django.db import models

# Create your models here.

class budget(models.Model):
    category = models.CharField(max_length=100, null=False, blank=False)
    num_of_budgets = models.IntegerField()

    def __str__(self):
        return f'{self.category} - {self.num_of_budgets}'
        
