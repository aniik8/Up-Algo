from django.db import models

# Create your models here.
class Discussion(models.Model):
    heading = models.TextField()
    content = models.TextField()
    slug = models.SlugField(max_length=20)
    user_id = models.IntegerField()
    likes = models.IntegerField()

    def __str__(self) -> str:
        return self.heading