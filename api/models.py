from django.db import models

# Relationship: BookNumber -> Book: 1:1


class BookNumber(models.Model):
    isbn_10 = models.CharField(max_length=10, blank=True)
    isbn_13 = models.CharField(max_length=13, blank=True)


class Book(models.Model):
    title = models.CharField(max_length=10, blank=False)
    description = models.TextField(max_length=256, blank=True)
    price = models.DecimalField(default=0, max_digits=3, decimal_places=2)
    published = models.DateField(blank=True, null=True, default=None)
    is_published = models.BooleanField(default=False)

    cover = models.ImageField(upload_to='covers/', blank=True)

    number = models.OneToOneField(
        BookNumber, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

# Relationship: Character -> Book: Many:1


class Character(models.Model):
    name = models.CharField(max_length=30)
    book = models.ForeignKey(
        Book, on_delete=models.CASCADE, related_name="characters")

    def __str__(self):
        return self.name

# Relationship: Character -> Book: Many:Many


class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    book = models.ManyToManyField(Book, related_name='authors')
