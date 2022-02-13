from django.db import models


class Contact(models.Model):
    name = models.CharField(max_length=100, unique=True, null=False)
    phone = models.CharField(max_length=100, unique=True, null=False)
    image = models.FileField(null=False, upload_to='avatars/')

    def __str__(self):
        return self.name
