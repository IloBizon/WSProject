from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=30)
    publication_date = models.DateField(auto_now_add=True)
    author = models.ManyToManyField('Author')
    genre = models.ManyToManyField('Genre')

    def __str__(self):
        return f'Книга {self.title}'

    def get_author(self):
        return ', '.join([i.name for i in self.author.all()])

    def get_genre(self):
        return ', '.join([i.name for i in self.genre.all()])

class Author(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'Автор {self.name}'

class Genre(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f'Жанр {self.name}'