from django.db import models


class Post(models.Model):
    """記事."""

    title = models.CharField(max_length=255)
    text = models.TextField()

    def __str__(self):
        return self.title
