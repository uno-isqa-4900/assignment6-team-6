from django.db import models
from io import BytesIO
from PIL import Image


class Genre(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField()

    class Meta:
        ordering = ('name',)
    
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f'/{self.slug}/'

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    bio = models.TextField()
    slug = models.SlugField()

    class Meta:
        ordering = ('last_name', 'first_name')
    
    def __str__(self):
        return f'{self.last_name}, {self.first_name}'

    def get_absolute_url(self):
        return f'/{self.slug}/'


class Book(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField()
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    genre = models.ForeignKey(Genre, related_name='books', on_delete=models.CASCADE)
    summary = models.TextField(blank=True, null=True)
    isbn = models.CharField('ISBN', max_length=13)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    image = models.ImageField(upload_to='uploads/', blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['title']
        index_together = ('id',) 
        
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f'/{self.genre.slug}/{self.slug}/'

    def get_image(self):
        if self.image:
            return 'http://127.0.0.1:8000' + self.image.url
        return ''
    