# Generated by Django 4.0.4 on 2022-04-27 08:26

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('photo', models.URLField(default=None)),
            ],
            options={
                'verbose_name': 'People',
                'verbose_name_plural': 'People',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Memory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=150)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.person')),
            ],
            options={
                'verbose_name': 'Memory',
                'verbose_name_plural': 'Memories',
            },
        ),
    ]