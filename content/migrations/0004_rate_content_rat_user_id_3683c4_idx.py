# Generated by Django 4.2.4 on 2023-08-26 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0003_alter_rate_rate'),
    ]

    operations = [
        migrations.AddIndex(
            model_name='rate',
            index=models.Index(fields=['user', 'content'], name='content_rat_user_id_3683c4_idx'),
        ),
    ]