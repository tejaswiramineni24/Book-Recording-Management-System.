from django.db import models

# Create your models here.
class book(models.Model):
    title=models.CharField(max_length=50)
    price=models.FloatField()
    Auther=models.CharField(max_length=50)
    Publisher=models.CharField(max_length=50)

    def __str__(self):
        return self.title
    