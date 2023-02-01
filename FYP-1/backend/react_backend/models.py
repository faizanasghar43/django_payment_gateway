from django.db import models

class Player_info(models.Model):
    name = models.CharField("Name", max_length=240)
    date = models.DateTimeField("Date")
    videofile = models.FileField(upload_to='videos/', null=True, verbose_name="")
    middled_count = models.IntegerField("Middled")
    edged_count = models.IntegerField("Edged")
    missed_count = models.IntegerField("Missed")

    def __str__(self):
        return { "Name ": self.name, "Balls Count" : self.balls_count,
                "Middled ": self.middled_count, "Edged": self.edged_count, "Missed":
                     self.missed_count}