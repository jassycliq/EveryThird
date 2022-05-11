from django.db import models


class Test(models.Model):
    string_to_cut = models.CharField(max_length=100, blank=True, default='')
