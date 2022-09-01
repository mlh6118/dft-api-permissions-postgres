from django.contrib.auth import get_user_model
from django.db import models


class Movie(models.Model):
    reviewer = models.ForeignKey(get_user_model(), on_delete=models.CASCADE,
                                 null=True)
    title = models.TextField(max_length=40)
    review = models.TextField(default="")
    stars = models.SmallIntegerField(default="0")
    review_date = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
