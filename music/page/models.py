from django.db import models

class Song(models.Model):
    choice = models.CharField(max_length=122)
    def __str__(self):
        return self.choices



