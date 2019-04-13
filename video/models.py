from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()


class Video(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название', help_text='пиши буквы пальцами', default='Я название видео')
    url = models.URLField()
    description = models.TextField(null=True, blank=True)
    like = models.PositiveIntegerField(default=0)
    dislike = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Comment(models.Model):
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    like = models.PositiveIntegerField(default=0)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    video = models.ForeignKey(Video, on_delete=models.CASCADE)
# Create your models here.
