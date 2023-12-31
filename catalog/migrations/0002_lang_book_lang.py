# Generated by Django 4.1 on 2023-10-01 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lang',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Enter a book genre', max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='lang',
            field=models.ManyToManyField(help_text='Select a language for this book', to='catalog.lang'),
        ),
    ]
