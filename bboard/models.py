from django.db import models

class Bd(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    price = models.FloatField(null=True, blank=True)
    published = models.DateTimeField(auto_now=True, db_index=True)





# Create your models here.
