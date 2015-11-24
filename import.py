import os, sys, string, csv, datetime, time, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sharks.settings")
from django.conf import settings
from attacks.models import Shark
from django.template.defaultfilters import slugify, urlize
reader = csv.reader(open("AttackData.csv", "rU"), dialect=csv.excel)
reader.next()
for row in reader:
    species = row[0]
    nom = row[1]
    nom_slug = slugify(nom)
    total = row[4]
    fatal = row[3]
    non = row[2] 
    a, acreated = Shark.objects.get_or_create(name=nom, name_slug=nom_slug, scientific_name=species, nonfatal=non, fatal=fatal, total=total)
    print a
