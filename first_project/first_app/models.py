from django.db import models

class HotelChain(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    state = models.SmallIntegerField()
    order = models.IntegerField()

    def __int__(self):
        return self.id
    def __str__(self):
        return self.name
    def __int__(self):
        return self.state
    def __int__(self):
        return self.order

class Hotel(models.Model):
    id = models.AutoField(primary_key=True)
    chain_id = models.ForeignKey(to=HotelChain, on_delete=models.CASCADE,
                                   default=0)
    name = models.CharField(max_length=255)
    alias = models.CharField(max_length=255, unique=True)
    star = models.IntegerField()
    web_address = models.CharField(max_length=255)
    telephone = models.CharField(max_length=255)
    fax = models.CharField(max_length=255)
    created_date = models.DateField()


    def __str__(self):
        return self.alias
    def __int__(self):
        return self.star
    def __str__(self):
        return self.web_address
    def __str__(self):
        return self.telephone
    def __str__(self):
        return self.fax
    def __str__(self):
        return str(self.created_date)
    def __str__(self):
        return self.name



# Create your models here.
