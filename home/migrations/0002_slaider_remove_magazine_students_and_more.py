# Generated by Django 4.0.5 on 2022-06-11 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Slaider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('photo', models.ImageField(upload_to='photo/')),
            ],
        ),
        migrations.RemoveField(
            model_name='magazine',
            name='students',
        ),
        migrations.RemoveField(
            model_name='students',
            name='class_name',
        ),
        migrations.DeleteModel(
            name='Classes',
        ),
        migrations.DeleteModel(
            name='Magazine',
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]
