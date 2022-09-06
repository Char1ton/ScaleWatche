from django.db import models

# Create your models here.

class ScaleWatcher(models.Model):
    title=models.CharField(max_length=120)
    description=models.TextField()
    line=models.CharField(max_length=120)

    def _str_(self):
        return self.title
