# Generated by Django 2.1.7 on 2019-05-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_spam', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_orders',
            name='id',
        ),
        migrations.AlterField(
            model_name='user_orders',
            name='email_id',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]