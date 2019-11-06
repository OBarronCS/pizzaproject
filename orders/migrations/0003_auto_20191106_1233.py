# Generated by Django 2.2.6 on 2019-11-06 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20191106_1232'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sub',
            name='size',
        ),
        migrations.AddField(
            model_name='submaintopping',
            name='size',
            field=models.CharField(choices=[('S', 'Small'), ('L', 'Large')], default='S', max_length=1),
        ),
    ]