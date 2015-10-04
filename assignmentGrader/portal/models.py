from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserProfile(models.Model):
    user = models.OneToOneField(User)

    profile_pic = models.ImageField(upload_to='profile_images', blank=True)
    StaffMember = models.BooleanField(default=False)

    def __unicode__(self):
        return self.user.username

class Problems(models.Model):

    #status of the problem
    problem_description = models.TextField()
    problem_title = models.CharField(max_length=20)
    test_cases = models.TextField()
    answer_file = models.TextField()
    user = models.ManyToManyField(User)

