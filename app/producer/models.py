from django.db import models


class Items(models.Model):
    id = models.CharField(max_length=50)
    itemId = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    iconUrl = models.CharField(max_length=50)
    mallId = models.CharField(max_length=50)
    keyword = models.CharField(max_length=50)

    def __str__(self):
        return self.keyword
