from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
# Create your models here.

#USER MODEL FROM DJANGO LINKED WITH THIS MODEL
class UserProfile(models.Model):
    """Substitutes default user of django and add new attributes to check."""
    user = models.OneToOneField(User,on_delete=models.CASCADE)#uses user created by django
    profile_points = models.PositiveIntegerField(default=80)
    
    #voyages
    portugal = models.BooleanField(default=False,verbose_name="portugal")
    andalusia = models.BooleanField(default=False,verbose_name="andalusia")
    nubia = models.BooleanField(default=False,verbose_name="nubia")
    england = models.BooleanField(default=False,verbose_name="england")
    brazil = models.BooleanField(default=False,verbose_name="brazil")

    def add_points(self,quantity):
        """Adds a (quantity) to profile_points in UserProfile model"""
        self.profile_points += quantity
        self.save()

    
    def sub_points(self,quantity):
        """Subtracts a (quantity) from profile_points in UserProfile model"""
        self.profile_points -= quantity
        self.save()

    def __str__(self):
        #name will appear because of this method
        return self.user.username

def create_profile(sender, **kwargs):
    """Creates profile for new user."""
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)