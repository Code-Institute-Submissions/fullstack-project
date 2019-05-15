from django.db import models
# Create your models here.
class Category(models.Model):
    name = models.CharField(blank=False,max_length=255)
    
    def __str__(self):
        return self.name

class Review(models.Model):
    review = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.review


class Product(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='posts', null=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='posts', null=True)

    def __str__(self):
        return self.name

