
from datetime import time
from django.db import models
from django.utils import timezone
# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=100)
    body=models.TextField()
    created=models.DateTimeField(default=timezone.now().replace(microsecond=0))
    updated=models.DateTimeField(default=timezone.now().replace(microsecond=0))

    class Meta:
        db_table='Core'
    
    def save(self, *args,**kwargs) :
        
        self.updated=timezone.now().replace(microsecond=0)
        super().save(*args,**kwargs)

        print('saved!')

class Author(models.Model):
    name=models.CharField(max_length=100)
    profession=models.TextField()
    created=models.DateTimeField(default=timezone.now().replace(microsecond=0))
    updated=models.DateTimeField(default=timezone.now().replace(microsecond=0))

    class Meta:
        db_table='Author'
    
    def __str__(self) -> str:
        return f"{self.name}"

class Book(models.Model):
    author=models.ManyToManyField(Author)
    title=models.CharField(max_length=100)
    created=models.DateTimeField(default=timezone.now().replace(microsecond=0))
    updated=models.DateTimeField(default=timezone.now().replace(microsecond=0))

    class Meta:
        db_table='Book'

    def __str__(self) -> str:
        return f"{self.title}"