from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Contributor

# @receiver(post_save, sender=User)
# def create_contributor(sender, instance, created, **kwargs):
#     if created:
#         Contributor.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_contributor(sender, instance, **kwargs):
#     instance.contributor.save()
