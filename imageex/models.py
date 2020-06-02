from django.db import models

# Create your models here.
class MyModel(models.Model):
    name = models.CharField(db_column='name', max_length=200, blank=False,unique=True)
    imageUrl = models.FileField(db_column='image_url', blank=True, null=True, upload_to='images/')

    class Meta:
        managed = True
        db_table = 'MyModel'