from django.db import models

# Create your models here.
class authorm(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    adress = models.CharField(max_length=30)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class bookm(models.Model):
    title = models.CharField(max_length=30)
    author = models.ForeignKey(authorm, on_delete=models.CASCADE)
    pb_year = models.IntegerField()
    isbn = models.CharField(max_length = 30)
    price = models.DecimalField(max_digits=10, decimal_places=2)