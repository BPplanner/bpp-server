# Generated by Django 3.2.4 on 2021-08-02 10:07

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
            name='LikeShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=20)),
                ('address', models.CharField(choices=[('gangnam', '강남구'), ('gangdong', '강동구'), ('gwangjin', '광진구'), ('mapo', '마포구'), ('seocho', '서초구')], max_length=20)),
                ('address_detail', models.TextField(max_length=50)),
                ('minprice', models.IntegerField()),
                ('price_desc', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_1', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_2', models.ImageField(blank=True, null=True, upload_to='')),
                ('profile_3', models.ImageField(blank=True, null=True, upload_to='')),
                ('map', models.ImageField(blank=True, null=True, upload_to='')),
                ('kakaourl', models.URLField(blank=True, null=True)),
                ('logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('shop_type', models.IntegerField(choices=[(0, 'studio'), (1, 'beautyshop')])),
                ('like_count', models.IntegerField(default=0)),
                ('affiliates', models.ManyToManyField(blank=True, null=True, related_name='_shop_shop_affiliates_+', to='shop.Shop')),
                ('like_users', models.ManyToManyField(blank=True, null=True, related_name='like_shops', through='shop.LikeShop', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='likeshop',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.shop'),
        ),
        migrations.AddField(
            model_name='likeshop',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
