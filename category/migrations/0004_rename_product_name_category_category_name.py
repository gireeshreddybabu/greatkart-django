# Generated by Django 3.2.4 on 2021-06-20 07:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0003_alter_category_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='product_name',
            new_name='category_name',
        ),
    ]