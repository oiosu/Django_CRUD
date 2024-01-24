from django.db import models
from django.urls import reverse

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/', null=True, blank=True)

    def get_absolute_url(self):
        return reverse('article_detail', args=[str(self.id)])