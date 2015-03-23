from django.db import models

# Create your models here.
class Datacenters(models.Model):
    name = models.CharField(max_length="64", unique=True)
    description = models.CharField(max_length="255")
    active = models.IntegerField(max_length="1", default=1)

    def __str__(self):
        return "%s" % (self.name)

    class Meta:
        db_table = 'location_datacenters'

class Cages(models.Model):
    name = models.CharField(max_length="64")
    datacenter = models.ForeignKey(Datacenters) #Links to Datacenters.id
    description = models.CharField(max_length="255")
    active = models.IntegerField(max_length="1", default=1)

    def __str__(self):
        return "%s.%s" % (self.name, self.datacenter.name)

    class Meta:
        db_table = 'location_cages'
        unique_together = (('name', 'datacenter'),)

class CageRows(models.Model):
    name = models.CharField(max_length="64")
    cage = models.ForeignKey(Cages) #Links to Cages.id
    description = models.CharField(max_length="255")
    active = models.IntegerField(max_length="1", default=1)

    def __str__(self):
        return "%s.%s.%s" % (self.name, self.cage.name, self.cage.datacenter.name)

    class Meta:
        db_table = 'location_cagerows'
        unique_together = (('name', 'cage'),)

class Racks(models.Model):
    name = models.CharField(max_length="64")
    cagerow = models.ForeignKey(CageRows) #Links to CageRows.id
    description = models.CharField(max_length="255")
    active = models.IntegerField(max_length="1", default=1)

    def __str__(self):
        return "%s.%s.%s.%s" % (self.name, self.cagerow.name, self.cagerow.cage.name, self.cagerow.cage.datacenter.name)

    class Meta:
        db_table = 'location_racks'
        unique_together = (('name', 'cagerow'),)