from django.db import models

# Create your models here.
class Posts(models.Model):
    userId = models.IntegerField()
    title = models.TextField(max_length = 500)
    body = models.TextField(max_length = 1000)

    def __str__(self):
        return self.title
