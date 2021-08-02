# Generated by Django 3.2.4 on 2021-08-02 10:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shop', '0001_initial'),
        ('concept', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studioconcept',
            name='like_users',
            field=models.ManyToManyField(blank=True, null=True, related_name='like_studio_concepts', through='concept.LikeStudioConcept', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='studioconcept',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studio_concepts', to='shop.shop'),
        ),
        migrations.AddField(
            model_name='likestudioconcept',
            name='studio_concept',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='concept.studioconcept'),
        ),
        migrations.AddField(
            model_name='likestudioconcept',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='beautyshopconcept',
            name='shop',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beautyshop_concepts', to='shop.shop'),
        ),
    ]
