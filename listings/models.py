from django.db import models
from roomtypes.models import Roomtype

# Create your models here.


class Listing(models.Model):
    room_type  = models.ForeignKey(Roomtype, on_delete=models.DO_NOTHING)
    booking_date = models.DateField()
    no_of_room_available_for_roomtype = models.IntegerField()
    max_no_of_room_for_roomtype = models.IntegerField()
    price = models.IntegerField()
    with_breakfast_price = models.IntegerField()
    with_breakfast = models.BooleanField(default=True)
    
    def __str__(self):
        return self.room_type