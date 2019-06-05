# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Album(models.Model):
    artist = models.CharField(max_length = 250)
    album_title = models.CharField(max_length = 500)
    genre = models.CharField(max_length = 100)
    album_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.artist + ' - ' + self.album_title

class Song(models.Model):
    album = models.ForeignKey(Album, on_delete = models.CASCADE)
    file_type = models.CharField(max_length = 10)
    song_title = models.CharField(max_length = 250)

class Sectors(models.Model):
    sector_name = models.CharField(max_length = 250)
    sector_logo = models.CharField(max_length = 1000)

    def __str__(self):
        return self.sector_name

class Company(models.Model):
    sector = models.ForeignKey(Sectors, on_delete = models.CASCADE)
    company_name = models.CharField(max_length = 250)

    def __str__(self):
        return self.company_name
