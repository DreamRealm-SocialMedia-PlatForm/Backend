from django.contrib.auth.models import AbstractUser
from django.db import models
import os

class DreamUser(AbstractUser):
    thumbnail   = models.ImageField(upload_to='thumbnails', null=True, blank=True)
    
    def save(self, *args, **kwargs):
        try:
            old_instance = DreamUser.objects.get(pk=self.pk)
            if old_instance.thumbnail and old_instance.thumbnail != self.thumbnail:
                if os.path.isfile(old_instance.thumbnail.path):
                    os.remove(old_instance.thumbnail.path)
        except :
            pass
        return  super().save(*args, **kwargs)
    
    def delete(self, *args, **kwargs):
            if self.thumbnail and os.path.isfile(self.thumbnail.path):
                os.remove(self.thumbnail.path)
            super().delete(*args, **kwargs)

