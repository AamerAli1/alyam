from django.db import models

# Create your models here.
class Pin (models.Model):
    """This Pin will be updated every 24 hours and used instead of password"""

    passcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__ (self):
        return self.passcode


class UserUsed(models.Model):
    name = models.CharField(max_length=200)
    passcode = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)


    def __str__ (self):
        return self.name

