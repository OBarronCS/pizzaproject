# Generated by Django 2.2.6 on 2019-11-04 22:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pasta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediant', models.CharField(max_length=64)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Platter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], default='S', max_length=1)),
                ('ingrediant', models.CharField(max_length=64)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Salad',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingrediant', models.CharField(max_length=64)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=3)),
            ],
        ),
        migrations.CreateModel(
            name='Sub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], default='S', max_length=1)),
                ('ingrediant', models.CharField(max_length=64)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Topping',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Pizza',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('size', models.CharField(choices=[('S', 'Small'), ('L', 'Large')], default='S', max_length=1)),
                ('type', models.CharField(choices=[('R', 'Regular'), ('S', 'Sicilian')], default='R', max_length=1)),
                ('cost', models.DecimalField(decimal_places=2, max_digits=4)),
                ('toppings', models.ManyToManyField(blank=True, related_name='pizzas', to='orders.Topping')),
            ],
        ),
    ]
