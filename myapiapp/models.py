from django.db import models

class CategoryMaster(models.Model):
    id = models.CharField(max_length=100, unique=True,primary_key=True)
    categoryName =  models.CharField(max_length=100, unique=True)
    parentName =  models.CharField(max_length=100)



class EventMaster(models.Model):
    id = models.CharField(max_length=100, unique=True,primary_key=True)
    eventName = models.CharField(max_length=100, unique=True)
    place = models.CharField(max_length=100)
    time = models.CharField(max_length=100)
    duration = models.CharField(max_length=100)
    cast = models.CharField(max_length=100)
    categoryName = models.ForeignKey(CategoryMaster, on_delete=models.CASCADE)


