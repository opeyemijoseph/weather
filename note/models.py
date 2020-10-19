from django.db import models

# Create your models here.

class Note(models.Model):
    post = models.TextField(max_length=100)

    def __str__(self):
        return self.post

    class Meta:
        verbose_name_plural = 'posts'

def get_absolute_url(self):
    return f'/notes/{self.id}/'