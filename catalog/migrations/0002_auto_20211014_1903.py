# Generated by Django 3.2.7 on 2021-10-14 17:03

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paintingdetailpage',
            name='categories',
        ),
        migrations.CreateModel(
            name='PaintingPagePaintingCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='catalog.paintingdetailpage')),
                ('painting_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='post_pages', to='catalog.paintingcategory')),
            ],
            options={
                'unique_together': {('page', 'painting_category')},
            },
        ),
    ]
