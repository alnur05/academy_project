# Generated by Django 4.2.6 on 2023-10-08 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('market', '0003_courseforuser_user_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseForUser2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('user_name', models.CharField(max_length=255)),
                ('user_id', models.IntegerField(default=0)),
            ],
        ),
    ]
