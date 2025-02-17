from django.contrib.auth.models import User
from django.db import models

class ReadBook(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField()
    main_characters = models.TextField()
    description = models.TextField()
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])

    def __str__(self):
        return f"{self.title} ({self.user.username})"
