from django.db import models



class Image(models.Model):
    user = models.ForeignKey('auth.User')
    picture = models.FileField()

    @property
    def image_url(self):
        if self.picture:
            return self.picture.url
        return "/"
