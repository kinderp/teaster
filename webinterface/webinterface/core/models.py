from django.db import models

# Create your models here.

from django.contrib.auth.models import User


class ProductType(models.Model):
    name = models.CharField(max_length=20, unique=True)
    
    def __str__(self):
        return "{}".format(self.name)

    def get_json(self):
        return {
            'name': self.name,
            'id': self.id
        }

class Product(models.Model):
    product_type = models.ForeignKey(ProductType, on_delete=models.PROTECT)
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=10)

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'version': self.version,
            'product_type': self.product_type.get_json()
        }

    def __str__(self):
        product = {
            'name': self.name,
            'version': self.version
        }
        return "{name} {version}".format(**product)
    
    class Meta:
        unique_together = (("name","version"),)

class Bug(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500) 
    c_date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    product = models.ManyToManyField(Product, through='BugProductStatus')

    def get_json(self):
        return {
            'name': self.name,
            'description': self.description,
            'c_date': self.c_date,
            'user': self.user.username,
            'product': [elem.get_json() for elem in self.bugproductstatus_set.all() ]
        }

class BugStatusType(models.Model):
    name = models.CharField(max_length=10, unique=True)
    description = models.CharField(max_length=100)
    
    def get_json(self):
        return {
            'name': self.name,
            'description': self.description
        }

    def __str__(self):
        return "{}".format(self.name)

class BugProductStatus(models.Model):
    status = models.ForeignKey(BugStatusType, on_delete=models.PROTECT)
    bug = models.ForeignKey(Bug, on_delete=models.PROTECT)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)
    bsc = models.CharField(max_length=100, unique=True)

    def get_json(self):
        return {
            'status': self.status.get_json(),
            'product': self.product.get_json(),
            'bsc': self.bsc
        }

class Discussion(models.Model):
    c_date = models.DateTimeField(auto_now_add=True)
    bug = models.OneToOneField(Bug, on_delete=models.PROTECT)


class Message(models.Model):
    c_date = models.DateTimeField(auto_now_add=True)
    u_date = models.DateTimeField(auto_now=True)
    text = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    discussion = models.ForeignKey(Discussion, on_delete=models.PROTECT)



class Resource(models.Model):
    bsc = models.CharField(max_length=100)
    comment = models.CharField(max_length=500)
    c_date = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=300) 


class LocationType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)


class Location(models.Model):
    url = models.CharField(max_length=500)
    location_type = models.ForeignKey(LocationType, on_delete=models.PROTECT)


class Source(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.OneToOneField(Location, on_delete=models.PROTECT)


class PackageType(models.Model):
    name = models.CharField(max_length=10, unique=True)


class Package(models.Model):
    name = models.CharField(max_length=100)
    version = models.CharField(max_length=10)
    package_type = models.ForeignKey(PackageType, on_delete=models.PROTECT)

    class Meta:
        unique_together = (("name", "version"),)


class EnvironmentType(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.CharField(max_length=500)


class Environment(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(max_length=500)
    c_date = models.DateTimeField(auto_now_add=True)
    u_date = models.DateTimeField(auto_now=True)
    location = models.OneToOneField(Location, on_delete=models.PROTECT)
    environment_type = models.ForeignKey(EnvironmentType, on_delete=models.PROTECT)
    source = models.OneToOneField(Source, on_delete=models.PROTECT)
    package = models.ManyToManyField(Package)
    product = models.ForeignKey(Product, on_delete=models.PROTECT)


class Tuple(models.Model):
    environment = models.ForeignKey(Environment, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    c_date = models.DateTimeField(auto_now_add=True)


class Reproducer(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500)
    location = models.OneToOneField(Location, on_delete=models.PROTECT)
    triple = models.OneToOneField(Tuple, on_delete=models.PROTECT)



