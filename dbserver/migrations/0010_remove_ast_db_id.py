# Generated by Django 3.2.8 on 2021-10-16 12:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dbserver', '0009_rename_db_index_ast_db_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ast',
            name='db_id',
        ),
    ]
