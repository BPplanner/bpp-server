# Generated by Django 3.2.4 on 2021-07-27 05:25

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BeautyShopConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ImageField(upload_to='')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StudioConcept',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('profile', models.ImageField(upload_to='')),
                ('head_count', multiselectfield.db.fields.MultiSelectField(choices=[(1, '1인'), (2, '2인'), (3, '3인이상')], max_length=5)),
                ('gender', multiselectfield.db.fields.MultiSelectField(choices=[('man', '남성'), ('woman', '여성')], max_length=9)),
                ('background', multiselectfield.db.fields.MultiSelectField(choices=[('all', '전체'), ('white', '흰색'), ('black', '검은색'), ('chromatic', '유채색'), ('etc', '기타배경'), ('outside', '야외')], max_length=37)),
                ('prop', multiselectfield.db.fields.MultiSelectField(choices=[('all', '전체'), ('health', '헬스도구'), ('mini', '소가구'), ('etc', '기타소품')], max_length=19)),
                ('dress', multiselectfield.db.fields.MultiSelectField(choices=[('all', '전체'), ('athleisure', '애슬레저'), ('swimsuit', '수영복'), ('underwear', '언더웨어'), ('etc', '기타')], max_length=37)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
