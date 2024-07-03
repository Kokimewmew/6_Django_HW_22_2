# Generated by Django 4.2.2 on 2024-07-02 17:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0006_product_user'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['category', 'title'], 'permissions': [('can_canceled_public', 'может отменять публикацию продукта'), ('can_edit_desk', 'может менять описание любого продукта'), ('can_edit_category', 'может менять категорию любого продукта')], 'verbose_name': 'Продукт', 'verbose_name_plural': 'Продукты'},
        ),
    ]