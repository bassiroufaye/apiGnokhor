# Generated by Django 2.2.1 on 2019-06-14 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apiGnokhor', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='image',
            field=models.FileField(blank=True, upload_to='post_image'),
        ),
    ]
