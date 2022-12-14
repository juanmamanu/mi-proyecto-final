# Generated by Django 4.1.2 on 2022-10-28 01:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_configuracion_subtitutulo_principal_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('short_content', models.CharField(max_length=255)),
                ('content', models.TextField(max_length=3000)),
                ('date_published', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
