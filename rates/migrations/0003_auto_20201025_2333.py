# Generated by Django 2.2.8 on 2020-10-25 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rates', '0002_auto_20201025_2236'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.ImageField(blank='true', default='default.png', upload_to='profile/'),
        ),
    ]
