# Generated by Django 5.1.7 on 2025-03-20 02:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gestor', '0003_item'),
    ]

    operations = [
        migrations.CreateModel(
            name='Type',
            fields=[
                ('TYPE_ID', models.AutoField(primary_key=True, serialize=False)),
                ('TYPE_NAME', models.CharField(max_length=20)),
            ],
        ),
        migrations.RenameField(
            model_name='genero',
            old_name='id',
            new_name='GENERO_ID',
        ),
        migrations.RenameField(
            model_name='genero',
            old_name='name',
            new_name='GENERO_NAME',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='current_chapter',
            new_name='ITEM_CURRENT_CHAPTER',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='ITEM_ECRIPTION',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='generos',
            new_name='ITEM_GENRES',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='id',
            new_name='ITEM_ID',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='on_going',
            new_name='ITEM_ON_GOING',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='title',
            new_name='ITEM_TITLE',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='url',
            new_name='ITEM_URL',
        ),
        migrations.RemoveField(
            model_name='item',
            name='tipo',
        ),
        migrations.AddField(
            model_name='item',
            name='ITEM_TYPE',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestor.type'),
        ),
    ]
