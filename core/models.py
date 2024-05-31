from django.db import models
import uuid
from django.conf import settings
# Create your models here.
class Movie(models.Model):
    Genre_Choices=[
        ('action','Action'),
        ('comedy','Comedy'),
        ('drama','Drama'),
        ('horror','Horror'),
        ('romance','Romance'),
        ('sci-fi','Sci-Fi'),
        ('fantasy','Fantasy')
    ]
    uu_id= models.UUIDField(default=uuid.uuid4)
    title=models.CharField(max_length=225)
    description=models.TextField()
    release_date=models.DateField()
    genre=models.CharField(max_length=100,choices=Genre_Choices)
    length=models.PositiveIntegerField(default=0)
    image_card=models.ImageField(upload_to='movies_images/')
    image_cover=models.ImageField(upload_to='movies_images/')
    video = models.FileField(upload_to="movies_videos/")
    movie_views=models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.title
class MovieList(models.Model):
    owner_user =models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    movie =models.ForeignKey(
            Movie,
            on_delete=models.CASCADE)