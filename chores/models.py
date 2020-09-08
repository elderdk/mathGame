from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Chore(models.Model):
    name = models.CharField(max_length = 250)
    score = models.IntegerField()
    duration = models.DurationField()
    description = models.CharField(max_length = 1000)
    user_assign = models.ManyToManyField(User)

    def __str__(self):
        return self.name

class ChoreLog(models.Model):
    user_did = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'log_chore')
    chore_name = models.ForeignKey(Chore, on_delete = models.CASCADE)
    done_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.chore_name.name
