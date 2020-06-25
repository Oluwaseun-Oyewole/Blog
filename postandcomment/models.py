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
        return f'{self.title} ' + f'{self.content}'

    class Meta:
        db_table = 'post'


    # how to find the url to specific instance of a post
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})



class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_author = models.CharField(max_length=50)
    comment_content = models.TextField()
    comment_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.comment_author} ' + f'{self.comment_content}'

    class Meta:
        db_table = 'comment'


