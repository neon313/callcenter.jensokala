# Generated by Django 4.2 on 2023-06-18 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admindashbord', '0006_order_created_main'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250, null=True)),
                ('price', models.CharField(max_length=250, null=True)),
                ('inventory', models.CharField(max_length=250, null=True)),
                ('mainimage', models.URLField(null=True)),
                ('active', models.BooleanField(default=False)),
                ('code', models.CharField(max_length=250, null=True)),
                ('postalCode', models.CharField(max_length=250, null=True)),
            ],
        ),
    ]