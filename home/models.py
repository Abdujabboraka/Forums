from django.contrib.auth.models import User

from django.db import models

# Create your models here.



class Mavzu(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='mavzu_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.title}".capitalize()


class Comment(models.Model):
    mavzu = models.ForeignKey(Mavzu, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.author}'s comment on {self.mavzu.title}".capitalize()



