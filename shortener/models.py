from django.db import models
from .code_generator import code_generator
# Create your models here.


class ShortURL(models.Model):
    url = models.URLField(unique=True)
    code = models.CharField(max_length=7, null=True, unique=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.url

    def save(self, *args, **kwargs):
        self.code = code_generator()
        super(ShortURL, self).save(*args, **kwargs)
