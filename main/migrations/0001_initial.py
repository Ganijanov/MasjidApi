# Generated by Django 4.2.2 on 2023-06-30 13:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cauntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('cauntry', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='cauntry', to='main.cauntry')),
            ],
        ),
        migrations.CreateModel(
            name='Masque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('capacity', models.PositiveIntegerField()),
                ('bio', models.TextField()),
                ('admin', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='city', to='main.city')),
            ],
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_name', models.CharField(max_length=250)),
                ('l_name', models.CharField(max_length=250)),
                ('staff', models.IntegerField(choices=[(2, 'Imom hatib'), (3, 'Qori'), (1, 'Imom'), (4, 'Muazzin')])),
                ('bio', models.TextField()),
                ('image', models.ImageField(upload_to='hodim/')),
                ('masque', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masque', to='main.masque')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PrayerTime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frm', models.DateField()),
                ('morning', models.DateTimeField()),
                ('Afternoon', models.DateTimeField()),
                ('Evening', models.DateTimeField()),
                ('Night', models.DateTimeField()),
                ('Midnight', models.DateTimeField()),
                ('to', models.DateField()),
                ('masquet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masque_time', to='main.masque')),
            ],
        ),
        migrations.CreateModel(
            name='ImageMasque',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='masque/')),
                ('masqueimg', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='masque_photo', to='main.masque')),
            ],
        ),
    ]