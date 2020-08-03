from django.db import models

class Post(models.Model):

    GENRE = [
        ('COMEDY', 'comedy'),
        ('FICTION', 'fiction'),
        ('HORROR', 'horror'),
        ('THRILLER', 'thriller'),
        ('ROMANTIC', 'romantic'),
        ('FAMILY', 'family'),
        ('LIFESTYLE', 'lifestyle'),
        ('GAMING', 'gaming'),
        ('KNOWLEDGE', 'knowledge')
    ]

    name = models.CharField(max_length=50, null=False, blank=False)
    title = models.CharField(max_length=50)
    content = models.CharField(max_length=5000)
    content_genre = models.CharField(choices=GENRE, max_length=10)
    date = models.DateTimeField()

    def __str__(self):
        return self.title