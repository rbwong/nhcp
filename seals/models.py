from django.db import models
from geoposition.fields import GeopositionField
from django.contrib.auth.models import User

class Region(models.Model):
    name = models.CharField(max_length=50)
    name_fil = models.CharField(max_length=50, null=False, blank=False)
    svg = models.CharField(max_length=2000, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class Province(models.Model):
    name = models.CharField(max_length=50)
    name_fil = models.CharField(max_length=50, null=False, blank=False)
    region = models.ForeignKey(Region)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class LGU(models.Model):
    image = models.ImageField(upload_to = 'images/seals/', default = 'images/seals/no-img.jpg')
    name = models.CharField(max_length=50)
    name_fil = models.CharField(max_length=50, null=False, blank=False)
    image_thumbnail = models.ImageField(upload_to = 'images/seals/thumbnail/', default = 'images/seals/thumbnail/no-img.jpg')
    description = models.CharField(max_length=500, null=False, blank=False)
    description_fil = models.CharField(max_length=500, null=False, blank=False)
    province = models.ForeignKey(Province)
    location = GeopositionField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class SealInfo(models.Model):
    name = models.CharField(max_length=50)
    name_fil = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    description_fil = models.CharField(max_length=500, null=False, blank=False)
    seal = models.ForeignKey(LGU)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name


class SealProperty(models.Model):
    name = models.CharField(max_length=50)
    name_fil = models.CharField(max_length=50, null=False, blank=False)
    description = models.CharField(max_length=500, null=False, blank=False)
    description_fil = models.CharField(max_length=500, null=False, blank=False)
    svg = models.CharField(max_length=2000, null=False, blank=False)
    seal = models.ForeignKey(LGU)
    date_created = models.DateTimeField(auto_now_add=True)

    def __unicode__(self):
        return self.name