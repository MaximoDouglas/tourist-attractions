# Generated by Django 3.0.4 on 2020-03-26 02:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_attractions', '0008_auto_20200325_0044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='touristattraction',
            name='guid',
            field=models.CharField(default='ddmhcenvme', editable=False, max_length=10),
        ),
    ]
