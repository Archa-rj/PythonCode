from django.db import models

# Create your models here.
class place(models.Model):
    name=models.CharField(max_length=250)
    img=models.ImageField(upload_to='pics')
    des=models.TextField()

    def __str__(self):
        return self.name
class team(models.Model):
    img=models.ImageField(upload_to='img')
    name=models.CharField(max_length=250)
    exp=models.TextField()

    def __str__(self):
        return self.name