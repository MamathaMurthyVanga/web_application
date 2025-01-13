from django.db import models

# Create your models here.
class App(models.Model):
    app_icon = models.ImageField(upload_to='img')
    app_name = models.CharField(db_column='name', max_length=100)
    app_link = models.URLField(db_column='link', max_length=100)
    app_category = models.CharField(db_column='category', max_length=100)
    sub_category = models.CharField(db_column='subcategory', max_length=100)
    points  = models.IntegerField(default=1)

    class Meta:
        db_table = 'admin_app'
