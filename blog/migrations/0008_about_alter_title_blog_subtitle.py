# Generated by Django 4.1.2 on 2022-11-18 23:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_title_delete_configuracion_delete_usuarios'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title_about', models.CharField(max_length=30)),
                ('content_about', models.TextField(max_length=1000)),
            ],
        ),
        migrations.AlterField(
            model_name='title',
            name='blog_subtitle',
            field=models.CharField(max_length=50),
        ),
    ]
