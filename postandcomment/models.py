from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.title}, ' + f'{self.content}'

    class Meta:
        db_table = 'post'


    # how to find the url to specific instance of a post
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})


