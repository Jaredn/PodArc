from django.db import models

# Create your models here.
class Datacenters(models.Model):
    name = models.CharField(max_length="64")
    description = models.CharField(max_length="255")

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'location_datacenters'

class Cages(models.Model):
    name = models.CharField(max_length="64")
    datacenter = models.ForeignKey(Datacenters) #Links to Datacenters.id
    description = models.CharField(max_length="255")

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'location_cages'

class CageRows(models.Model):
    name = models.CharField(max_length="64")
    cage = models.ForeignKey(Cages) #Links to Cages.id
    description = models.CharField(max_length="255")

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'location_cagerows'

class Racks(models.Model):
    name = models.CharField(max_length="64")
    cage = models.ForeignKey(CageRows) #Links to CageRows.id
    description = models.CharField(max_length="255")

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'location_racks'