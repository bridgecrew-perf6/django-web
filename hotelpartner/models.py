from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify

# Create your models here.
class HotelChain(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    state = models.SmallIntegerField()
    order = models.IntegerField()
    def get_absolute_url(self):
        # return reverse('hotelpartner:detailhotelchain', args=[str(self.id)])
        return reverse('hotelpartner:detailhotelchain', kwargs={'pk' : int(self.id), 'slug' : slugify(self.name)})

    def __int__(self):
        return self.id
    def __str__(self):
        return self.name
    def __int__(self):
        return self.state
    def __int__(self):
        return self.order