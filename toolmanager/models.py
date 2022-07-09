from django.db import models

#TOOLS MODELS (NOT USED)

class Tool(models.Model):
    name = models.CharField(max_length=256)
    description = models.TextField(max_length=500,default="Description here")
    price = models.PositiveIntegerField(verbose_name="points",default=10)
    def __str__(self):
        return self.name