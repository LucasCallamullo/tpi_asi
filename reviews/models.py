

from django.db import models

# Create your models here.
class Review(models.Model):
    tutor = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey('users.CustomUser', on_delete=models.SET_NULL, null=True, blank=True, related_name='given_reviews')
    rating = models.IntegerField()  # ej: de 1 a 5
    comment = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # class Meta:
    #    unique_together = ('tutor', 'reviewer')  # evita duplicados