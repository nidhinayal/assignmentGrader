from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    profile_pic = models.ImageField(upload_to='profile_images', blank=True)
    StaffMember = models.BooleanField(editable=False, default=False)
    
    def __unicode__(self):
        return self.user.username


