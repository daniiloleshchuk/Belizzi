# Generated by Django 2.2.7 on 2019-11-17 13:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dessert',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='tested dessert', max_length=100)),
                ('category', models.CharField(default='Dessert', max_length=100)),
                ('preparing_time', models.CharField(default='10-15min', max_length=100)),
                ('components', models.CharField(default='one two three four five', max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=4)),
                ('img', models.ImageField(upload_to='Desserts')),
            ],
        ),
    ]
