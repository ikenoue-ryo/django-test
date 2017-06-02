from django.db import models


class Post(models.Model):
    """記事."""

    title = models.CharField('タイトル', max_length=255)
    text = models.TextField('本文')

    def __str__(self):
        return self.title
