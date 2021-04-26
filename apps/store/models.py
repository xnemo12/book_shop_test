from django.db import models


class Book(models.Model):
    title = models.CharField('Book name', max_length=255, null=False, blank=False)
    authors = models.CharField('Authors', max_length=255, null=False, blank=False)
    publisher = models.CharField('Publisher', max_length=255, null=True, blank=True)
    publication_date = models.DateField()
    description = models.TextField('Description', null=True, blank=True)

