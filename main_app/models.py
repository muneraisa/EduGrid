from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    capacity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.name} (cap {self.capacity})"


class Slot(models.Model):
    WEEKDAYS = [(i, d) for i, d in enumerate(["Sun", "Mon", "Tue", "Wed", "Thu", "Fri", "Sat"])]
    weekday = models.PositiveSmallIntegerField(choices=WEEKDAYS)
    start_time = models.TimeField()
    end_time = models.TimeField()

    class Meta:
        unique_together = ("weekday", "start_time", "end_time")

    def __str__(self):
        return f"{self.get_weekday_display()} {self.start_time}-{self.end_time}"


class Assignment(models.Model):
    course_name = models.CharField(max_length=200)                   
    teacher = models.ForeignKey(User, on_delete=models.CASCADE)     
    room = models.ForeignKey(Room, on_delete=models.CASCADE)        
    slot = models.ForeignKey(Slot, on_delete=models.CASCADE)         

    class Meta:
        unique_together = [
            ("teacher", "slot"),   
            ("room", "slot"),     
        ]

    def __str__(self):
        return f"{self.course_name} by {self.teacher} in {self.room} at {self.slot}"
