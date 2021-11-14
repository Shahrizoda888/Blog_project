from django.db import models
from django.db.models.fields.related import ForeignKey

# Create your models here.
class Post(models.Model):
    title=models.CharField(max_length=200)
    author=models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE
    )
    body=models.TextField()


    def __str__(self):
        return self.title