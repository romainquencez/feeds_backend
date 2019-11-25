# Generated by Django 2.2.7 on 2019-11-25 18:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('icon', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=150)),
                ('feed', models.URLField()),
                ('website', models.URLField(null=True)),
                ('language', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='feed.Language')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='category.Category')),
            ],
        ),
    ]
