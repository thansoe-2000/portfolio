from django.db import models

# Create your models here.
# category
class Category(models.Model):
    name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.name

# photo
class Photo(models.Model):
    title = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title
    
    