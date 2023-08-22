from django.db import models

# Create your models here.
class Job(models.Model):
    image = models.ImageField(upload_to = 'images/')
    summary = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    description = models.TextField()


    def __str__(self):
        return self.summary
