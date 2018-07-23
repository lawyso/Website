from django.conf import settings
from django.db import models
from django.db.models.signals import post_save


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'profile_image/user_{0}/{1}'.format(instance.user.id, filename)


User = settings.AUTH_USER_MODEL


class Profile(models.Model):
    gender_choices = (('male', 'male'),
                      ('female', 'female'))

    user = models.OneToOneField(User)
    tagline = models.CharField(max_length=50)
    description = models.TextField(max_length=300)
    avatar = models.ImageField(upload_to=user_directory_path,null=True)
    verified = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    dob = models.DateField(null=True)
    gender = models.CharField(choices=gender_choices, max_length=10)
    membership_no = models.CharField(max_length=50,blank=True)
    next_of_kin = models.CharField(max_length=50,blank=True)
    date_of_joining = models.DateField(null=True)

    def __str__(self):
        return self.user.username


def post_save_user_receiver(sender, instance, created, *args, **kwargs):
    if created:
        profile, is_created = Profile.objects.get_or_create(user=instance)

post_save.connect(post_save_user_receiver, sender=User)
