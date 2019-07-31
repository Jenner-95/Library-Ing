from django.db import models
from users.models import User


# Create your models here.
class Book(models.Model):
    GENRE_CHOICES = [
        (1, 'Horror'),
        (2, 'Fantasy'),
        (3, 'Mystery'),
        (4, 'Biography'),
        (5, 'Romance'),
        (6, 'Self Help'),
    ]
    LANGUAGE_CHOICES = [
        (1, 'English'),
        (2, 'Spanish'),
        (3, 'French'),
        (4, 'German'),
        (5, 'Chinese'),
    ]
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=50)
    genre = models.IntegerField(choices=GENRE_CHOICES)
    language = models.IntegerField(choices=LANGUAGE_CHOICES)
    publication_date = models.DateField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return self.name + ' (' + self.author.first_name + ' ' + self.author.last_name + ')'