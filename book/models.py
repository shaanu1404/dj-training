from django.db import models

from author.models import Author

class Book(models.Model):

    class BookType(models.TextChoices):
        novel = ('NOVEL', 'Novel')
        article = ('ARTICLE', 'Article')
        magzine = ('MAGZINE', 'Magzine')
        news = ('NEWS', 'News')

    title = models.CharField(max_length=120)
    description = models.TextField(null=True, blank=True)
    isbn = models.CharField(max_length=30)
    book_type = models.CharField(max_length=30, choices=BookType.choices)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    cover_image = models.ImageField(upload_to='images/', null=True, blank=True)
    excerpt = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title