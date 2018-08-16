from __future__ import unicode_literals
from django.db import models
from PIL import Image
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
# Create your models here.
class profile(models.Model):
    name=models.CharField(max_length=100)
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE,null=True, blank=True)
    description = models.TextField(default='description default text')

    def __unicode__(self):
        return self.name
class userStripe(models.Model):
    user=models.OneToOneField(settings.AUTH_USER_MODEL,on_delete = models.CASCADE)
    stripe_id=models.CharField(max_length=200, null=True)

    def __unicode__(self):
        if self.stripe_id:
            return  str(self.stripe_id)
        else:
            return self.user.username

# def my_callback(sender,request, user, **kwargs):
#     idStripe, created =userStripe.object.get_or_create(user=user)
#     if created:
#         print 'created'
#     userProfile, is_created=profile.object.get_or_create(user=user)
#     if is_created:
#         userProfile.name=user.username
#         userProfile.save()
#
# user_logged_in.connect(my_callback)


class data(models.Model):
    name=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    price=models.DecimalField(max_digits=50, decimal_places=5, default="")
    img=models.ImageField(upload_to='cart_image',blank=True)

    def __str__(self):
        return self.name
