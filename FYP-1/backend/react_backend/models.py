from django.db import models

class Player(models.Model):
    name = models.CharField("Name", max_length=240)
    balls_count = models.IntegerField("Balls")
    edged_count = models.IntegerField("Edged")
    missed_count = models.IntegerField("Missed")

    def __str__(self):
        return { "Name ": self.name, "Balls Count" : self.balls_count,
                "Edged": self.edged_count, "Missed":
                     self.missed_count}