# Generated by Django 2.1.7 on 2019-04-02 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0004_remove_item_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='name',
            field=models.CharField(default='Default Name', max_length=50),
            preserve_default=False,
        ),
    ]
