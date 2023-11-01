# Generated by Django 3.2.22 on 2023-11-01 17:46

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
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=80, unique=True)),
                ('date_created_on', models.DateTimeField(auto_now=True)),
                ('date_updated_on', models.DateTimeField(auto_now=True)),
                ('rate', models.PositiveSmallIntegerField()),
                ('review_text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='feedback', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-date_updated_on'],
            },
        ),
    ]