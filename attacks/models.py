from django.db import models

class Shark(models.Model):
    name=models.CharField(max_length=255)
    name_slug=models.SlugField()
    scientific_name=models.CharField(max_length=255) 
    nonfatal=models.IntegerField()
    fatal=models.IntegerField()
    total=models.IntegerField()
    photo=models.FileField(upload_to="photos/", blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    def get_absolute_url(self):
        return "sharks/%s" % self.name_slug
    def __unicode__(self):
    	return self.name

