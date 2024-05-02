from django.db import models

# Create your models here.
class Food(models.Model):
    name=models.CharField(max_length=200,unique=True)
    category=models.CharField(max_length=200)
    price=models.PositiveBigIntegerField()
    offer=models.PositiveBigIntegerField()
    

    def __str__(self):
        return self.name

