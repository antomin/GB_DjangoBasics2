# Generated by Django 3.2.12 on 2022-03-15 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0006_shopuserprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='shopuserprofile',
            name='country',
            field=models.CharField(blank=True, max_length=50, verbose_name='страна'),
        ),
        migrations.AlterField(
            model_name='shopuserprofile',
            name='about_me',
            field=models.TextField(blank=True, max_length=512, verbose_name='о себе'),
        ),
    ]