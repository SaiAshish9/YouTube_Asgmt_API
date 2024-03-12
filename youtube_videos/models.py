from django.db import models

# Create your models here.

class Video(models.Model):

    def __str__(self):
        return self.id

    id = models.CharField(max_length=255, primary_key=True, null=False)
    title = models.CharField(max_length=255, null=False)
    description = models.CharField(max_length=255, null=False)
    publishing_date = models.DateTimeField(null=False)
    thumbnail_urls = models.CharField(max_length=255, null=False)
    view_count = models.CharField(max_length=255)
    duration = models.CharField(max_length=255)
