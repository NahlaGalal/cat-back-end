# Generated by Django 3.0.5 on 2020-09-02 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='auther',
            new_name='author',
        ),
        migrations.AddField(
            model_name='article',
            name='image',
            field=models.ImageField(default=1, upload_to='blogs_pics'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]