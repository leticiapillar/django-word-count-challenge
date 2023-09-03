from django.db import models

# Create your models here.
class WordCountModel(models.Model):
    text = models.TextField()
    total_words = models.IntegerField()
    
    def __str__(self):
        return (
            f"text={self.text[:30]}...\n"
            f"total_words={self.total_words}"
        )
