# Generated by Django 2.1.7 on 2019-05-07 06:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin_Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_username', models.CharField(max_length=20)),
                ('a_password', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('comment', models.TextField()),
                ('rate', models.IntegerField()),
                ('email', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Upload_Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_category', models.CharField(max_length=10)),
                ('product_name', models.CharField(max_length=20)),
                ('product_brand', models.CharField(max_length=20)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('upload_image', models.ImageField(upload_to='loki/')),
            ],
        ),
        migrations.CreateModel(
            name='User_Login',
            fields=[
                ('u_username', models.CharField(max_length=20)),
                ('u_password', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
            ],
        ),
        migrations.CreateModel(
            name='user_Orders',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=20)),
                ('product_brand', models.CharField(max_length=20)),
                ('product_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('upload_image', models.ImageField(upload_to='orders/')),
                ('email_id', models.EmailField(max_length=254)),
            ],
        ),
    ]
