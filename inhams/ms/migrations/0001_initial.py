# Generated by Django 2.2.4 on 2020-02-21 16:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Word',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('writer', models.CharField(max_length=50)),
                ('content', models.TextField()),
            ],
        ),
    ]
