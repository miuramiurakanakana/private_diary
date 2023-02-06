# Generated by Django 3.2.7 on 2023-02-06 01:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0003_auto_20230206_1002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='diary',
            name='content',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='photo1',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='photo2',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='photo3',
        ),
        migrations.RemoveField(
            model_name='diary',
            name='title',
        ),
        migrations.AlterField(
            model_name='diary',
            name='市町村',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='市町村'),
        ),
    ]
