from django.db import models

# Create your models here.

class User(models.Model):
    class Meta:
        db_table = 'user'
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=48, unique=True, null=False)
    email = models.CharField(max_length=64, unique=True, null=False)
    password = models.CharField(max_length=128, null=False)

    def __repr__(self):
        return '<user {} {}>'.format(self.id, self.name)

    __str__ = __repr__
