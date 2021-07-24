# Generated by Django 3.2.4 on 2021-07-24 02:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('shop', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PickShop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('state', models.IntegerField(default=0)),
                ('reserved_date', models.DateTimeField(blank=True, null=True)),
                ('pick_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickshop', to=settings.AUTH_USER_MODEL)),
                ('shop', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pickshop', to='shop.shop')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]