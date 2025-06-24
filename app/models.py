# models.py

from django.db import models

class Formula(models.Model):
    name = models.CharField(max_length=100)
    expression = models.TextField(help_text="Write formula like a + b * c - d / e")
    variables = models.JSONField(help_text='List of variables like ["a", "b", "c", "d", "e"]')

    def __str__(self):
        return self.name
