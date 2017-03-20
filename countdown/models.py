from django.db import models

class Countdown(models.Model):
    base_slug = models.CharField(max_length=50)
    management_slug = models.CharField(max_length=50)

class Image(models.Model):
    countdown = models.ForeignKey(Countdown)
    picture = models.FileField()

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "/"
