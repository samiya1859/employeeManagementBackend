from django.db import models
from PIL import Image
# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=150)
    phone = models.CharField(max_length=20)
    birth = models.DateField()
    image = models.ImageField(upload_to='images/',null=True,blank=True)

    def save(self,*args, **kwargs):
        super().save(*args,**kwargs)
        if self.image:
            img = Image.open(self.image.path)
            if img.height > 300 or img.width > 300:
                output_size = (300, 300)
                img.thumbnail(output_size)
                img.save(self.image.path)
           

    def __str__(self):
         return f"{self.first_name} {self.last_name}"