# Generated by Django 4.0.4 on 2022-05-05 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('Pop Music', 'Pop Music'), ('Jazz Music', 'Jazz Music'), ('R&B Music', 'R&B Music'), ('Rock Music', 'Rock Music'), ('Country Music', 'Country Music'), ('Dance Music', 'Dance Music'), ('Hip Hop Music', 'Hip Hop Music'), ('Other', 'Other')], max_length=30),
        ),
    ]
