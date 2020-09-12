from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Chore(models.Model):
    name = models.CharField(max_length = 250)
    score = models.IntegerField()
    description = models.CharField(max_length = 1000)
    user_assign = models.ManyToManyField(User)
    image = models.ImageField(upload_to='chore_images', default='cat.png')
    show_by_image = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)

class ChoreLog(models.Model):
    user_did = models.ForeignKey(User, on_delete = models.CASCADE, related_name = 'log_chore')
    chore_name = models.ForeignKey(Chore, on_delete = models.CASCADE)
    done_time = models.DateTimeField(auto_now = True)

    def __str__(self):
        return self.chore_name.name
