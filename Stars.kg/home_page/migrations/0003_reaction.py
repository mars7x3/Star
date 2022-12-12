# Generated by Django 4.1 on 2022-12-12 17:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('star_all', '0003_remove_starcomment_grade_starcomment_rating_and_more'),
        ('home_page', '0002_commenthomepage_examplehomepage_catalog'),
    ]

    operations = [
        migrations.CreateModel(
            name='Reaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('custom_id', models.IntegerField()),
                ('video', models.FileField(upload_to='home-comment-works')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='reactions', to='star_all.star')),
            ],
            options={
                'ordering': ['custom_id'],
            },
        ),
    ]
