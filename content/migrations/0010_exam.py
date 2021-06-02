# Generated by Django 3.2 on 2021-05-21 17:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_auto_20210521_1735'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exam',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titre', models.CharField(blank=True, max_length=200, null=True)),
                ('dec', models.CharField(blank=True, max_length=200, null=True)),
                ('dt', models.DateField(auto_now=True)),
                ('files', models.FileField(upload_to='Docs')),
                ('cour', models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='content.cour')),
            ],
        ),
    ]
