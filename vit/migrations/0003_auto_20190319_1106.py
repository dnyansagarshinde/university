# Generated by Django 2.1.7 on 2019-03-19 05:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vit', '0002_auto_20190316_1013'),
    ]

    operations = [
        migrations.AddField(
            model_name='enrolled',
            name='ass1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='ass2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='ass3',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='cat1',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='cat2',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AddField(
            model_name='enrolled',
            name='fat',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='enrolled',
            name='grade',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=6),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='salary',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
        migrations.AlterField(
            model_name='roomdetails',
            name='fees',
            field=models.DecimalField(decimal_places=2, max_digits=6),
        ),
    ]
