from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Contributor(models.Model):
    author = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500, default="")
    abstract = models.TextField(default="")
    key_words = models.CharField(max_length=500,default="")

    SPEACH = 'TK'
    INVITED = 'IT'
    POSTER = 'PO'
    CONTRIBUTION_CHOICES = [
        (SPEACH,'Talk'),
        (INVITED,'Invited Talk'),
        (POSTER,'Poster')
    ]
    contribution = models.CharField(
                   max_length=2,
                   choices=CONTRIBUTION_CHOICES,
                   default=SPEACH,
                   )
    bio = models.TextField(default="", verbose_name="Short Biography")
    selected = models.BooleanField(default=False)

    expertise = models.TextField(default="", verbose_name="What are your expertise?")
    tolearn = models.TextField(default="", verbose_name="What would you still like to learn?")

    welcome = models.BooleanField(default=False, verbose_name="I am joining the welcome evening (Wednesday 4th of November)")
    citytour = models.BooleanField(default=False, verbose_name="I am joining the guided city tour (FREE - Thursday 5th of November)")
    restaurant = models.BooleanField(default=False, verbose_name="I am joining the social dinner on Thursday 5th of November")

    def __str__(self):
        return '{}_{}'.format(self.author.first_name, self.author.last_name)

    def get_absolute_url(self):
        return reverse('home')
