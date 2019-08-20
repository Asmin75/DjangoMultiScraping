from django.db import models

# Create your models here.


class ScrapyItem(models.Model):
    start_url = models.CharField(max_length=5000)
    h3 = models.CharField(max_length=5000)
    h2 = models.CharField(max_length=5000)

    def __str__(self):
        return '%s %s %s' % (self.start_url, self.h3, self.h2)