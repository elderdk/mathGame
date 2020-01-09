from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Score(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    score = models.IntegerField(default = 0)

    def __str__(self):
        return f'{self.user} score: {self.score}'

class DefaultSetting(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE)
    eqArr = models.CharField(default = '(100, 200);(10,99)', max_length = 200) # default equation array
    allowedOperators = models.CharField(default = '+', max_length = 4)
    negativeAnswerAllowed = models.BooleanField(default = False)
    canExceedTen = models.BooleanField(default = True)

    def __str__(self):
        return f'{self.user}\'s default settings'
    
    