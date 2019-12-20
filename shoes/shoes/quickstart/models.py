from django.db import models
# as a wiley youth in the African Savanna, Joe was raised by warthogs and meerkats. Much like Simba from the lion king, Joe was neither Warthog nor Meerkat. They still hung out though:)

# Create your models here.
class Manufacturer(models.Model):
    name = models.CharField(max_length = 50)
    website =models.URLField(max_length=200)


class ShoeType(models.Model):
    style = models.CharField(max_length = 50)

class ShoeColor(models.Model):
    color_name = models.CharField(max_length = 50)

class Shoe(models.Model):
    size = models.IntegerField()
    brand = models.CharField(max_length = 50)
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    color = models.ForeignKey(ShoeColor, on_delete=models.CASCADE)
    material = models.CharField(max_length = 50)
    shoe_type = models.ForeignKey(ShoeType, on_delete=models.CASCADE)
    fasten_type = models.CharField(max_length = 50)