from django.db import models


class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    # fields
    class Meta:
        app_label = 'myapp'
        db_table = 'user'
