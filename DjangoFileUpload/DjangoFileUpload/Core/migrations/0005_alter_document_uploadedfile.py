# Generated by Django 4.0.4 on 2022-05-17 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_alter_document_uploadedfile_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='uploadedFile',
            field=models.CharField(max_length=200),
        ),
    ]
