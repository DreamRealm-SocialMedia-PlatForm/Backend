# Generated by Django 4.0.1 on 2024-10-08 08:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DreamCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='dream',
            name='category',
            field=models.ManyToManyField(related_name='dream', to='api.DreamCategory'),
        ),
    ]
