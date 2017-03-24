from django.db import models

class Countdown(models.Model):
    base_slug = models.CharField(max_length=50)
    management_slug = models.CharField(max_length=50)
    end_time = models.DateTimeField()
    email = models.CharField(null=True,blank=True,max_length=100)
    title = models.CharField(null=True,blank=True,max_length=25)

    def list_pictures(self):
        return [image for image in self.image_set.all()]

    def __str__(self):
        return self.email

class Image(models.Model):
    countdown = models.ForeignKey(Countdown)
    picture = models.FileField()

    def __str__(self):
        return self.image_url

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "/"
