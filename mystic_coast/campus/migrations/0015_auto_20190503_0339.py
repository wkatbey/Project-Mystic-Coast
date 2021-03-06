# Generated by Django 2.2 on 2019-05-03 07:39

import address.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('campus', '0014_auto_20190425_0602'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurant',
            name='friday',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='monday',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='saturday',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='sunday',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='thursday',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='tuesday',
        ),
        migrations.RemoveField(
            model_name='restaurant',
            name='wednesday',
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='description',
            field=models.CharField(default='No description added', max_length=300, verbose_name='Tell us abbout your restaurant!'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='location',
            field=address.models.AddressField(max_length=200, on_delete=django.db.models.deletion.CASCADE, to='address.Address', verbose_name='Location'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='name',
            field=models.CharField(max_length=200, verbose_name='Restaurant Name'),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='phone_number',
            field=models.CharField(default='(xxx) xxx-xxxx', max_length=20, verbose_name='(Primary) Phone Number'),
        ),
        migrations.CreateModel(
            name='BusinessHours',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opening_time', models.TimeField()),
                ('closing_time', models.TimeField()),
                ('restaurant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='campus.Restaurant')),
            ],
        ),
    ]
