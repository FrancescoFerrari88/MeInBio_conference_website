from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Contributor(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, default="")
    abstract = models.TextField(default="")
    key_words = models.CharField(max_length=500,default="")

    SPEACH = 'SP'
    POSTER = 'PO'
    CONTRIBUTION_CHOICES = [
        (SPEACH,'Speach'),
        (POSTER,'Poster')
    ]
    contribution = models.CharField(
                   max_length=2,
                   choices=CONTRIBUTION_CHOICES,
                   default=SPEACH,
                   )
    bio = models.TextField(default="")
    selected = models.BooleanField(default=False)

    def __str__(self):
        return '{}_{}'.format(self.author.first_name, self.author.last_name)

    def get_absolute_url(self):
        return reverse('home')
