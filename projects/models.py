from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Project(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    image = models.ImageField(upload_to='projects/images/')
    url = models.URLField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title + ' - by ' + self.user.username
