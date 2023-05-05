from django.db import models

# Create your models here.
class upload(models.Model):
    fname = models.CharField(max_length=150)
    lname = models.CharField(max_length=200)
    email = models.EmailField()
    file = models.FileField( null=True, blank=True)

    class Meta:
        db_table = "upload"