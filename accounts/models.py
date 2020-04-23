from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField
from django.db.models.signals import post_save
from django.dispatch import receiver


# student is not an option because that's the assumed default when teacher = false
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    grade = models.TextField(max_length=10, null=True, blank=True)
    is_super_student = models.BooleanField(default=False, null=False)
    is_tech = models.BooleanField(default=False, null=False)
    is_teacher = models.BooleanField(default=False, null=False)
    is_super_teacher = models.BooleanField(default=False, null=False)
    phone_number = PhoneNumberField(blank=True)

    # in some cases, a user does not have grade (teacher / test account) which would cause an error. => None check!
    def __str__(self):
        if self.grade is None:
            return self.user.username
        else:
            return f'{self.user.username + " | " + self.grade}'

    @property
    def user_name(self):
        return self.user.username

    @property
    def user_email(self):
        return self.user.email


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()
