from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.dispatch import receiver
from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token


# Create your models here.

# Extending AbstractUser offers these advantages:
# Django provides a built-in AbstractUser model that includes essential fields and functionality for user management.
# By extending AbstractUser, you inherit these features and can customize them without rebuilding everything from scratch.
# This approach saves time, ensures consistency with Django's conventions, and potentially provides better integration with other parts of Django.
# Built-in features: Leverages Django's existing user management functionality.
# Customization: Allows you to add specific fields and tailor the user model to your application's needs.
# Authentication and authorization: Integrates seamlessly with Django's authentication system.
# Maintainability: Benefits from updates and improvements to Django's core user model.


class IMUser(AbstractUser):
    first_name = models.CharField(max_length=155, blank=True)
    last_name = models.CharField(max_length=155, blank=True)
    middle_name = models.CharField(max_length=155, blank=True)
    phone_number = models.CharField(max_length=20, blank=True)

    USER_TYPES = [
        ('EIT', 'Entrepreneur-In-Training'),
        ('TEACHING_FELLOW', 'Teaching Fellow'),
        ('ADMIN_STAFF', 'Administrative Staff'),
        ('ADMIN', 'Administrator'),
    ]

    user_type = models.CharField(max_length=20, choices=USER_TYPES, default='EIT')
    date_created = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='imuser_set')
    user_permissions = models.ManyToManyField(Permission, related_name='imuser_set')
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"

@receiver(post_save, sender=IMUser)
def generate_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        token = Token.objects.create(user=instance)
        token.save()

class Cohort(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    year = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name} ({self.year})"
    
class CohortMember(models.Model):
    cohort = models.ForeignKey(Cohort, on_delete=models.CASCADE, related_name='members')
    member = models.ForeignKey(IMUser, on_delete=models.CASCADE, related_name='cohorts')
    is_active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(IMUser, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.member.first_name} {self.member.last_name} ({self.cohort.name})"
    
class Query(models.Model):
    user = models.ForeignKey(IMUser, on_delete=models.CASCADE)
    text = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def _str_(self):
        return f"{self.user.username} - {self.text}"