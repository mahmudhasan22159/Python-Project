from django.db import models

class SalesData(models.Model):
    date = models.DateField()
    product = models.CharField(max_length=100)
    quantity = models.IntegerField()
    revenue = models.FloatField()

    def __str__(self):
        return f"{self.product} - {self.date}"
