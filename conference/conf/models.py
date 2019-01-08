from django.db import models

class Room(models.Model):
    name = models.CharField(max_length=64)
    seats = models.IntegerField()
    projector = models.BooleanField()

class Reservation(models.Model):
    date = models.DateField()
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    comment = models.TextField()

    class Meta:
        unique_together = ('date', 'room')
