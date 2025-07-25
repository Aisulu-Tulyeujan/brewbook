# Generated by Django 5.2.2 on 2025-07-10 17:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brewbookapp', '0004_remove_drink_ingredients_ingredient'),
    ]

    operations = [
        migrations.CreateModel(
            name='Liked',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('drink', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='liked_drinks', to='brewbookapp.drink')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='Favorite',
        ),
    ]
