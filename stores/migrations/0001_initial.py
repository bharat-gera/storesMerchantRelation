# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('article_id', models.CharField(max_length=16, verbose_name='Article ID')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=512, verbose_name='Products')),
                ('price', models.FloatField(verbose_name='Price')),
                ('availabilty', models.BooleanField(default=False)),
                ('stock', models.IntegerField(default=0, verbose_name='Stock')),
            ],
        ),
        migrations.CreateModel(
            name='Store',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('store_name', models.CharField(help_text=b'Store name', max_length=128, verbose_name='Stores')),
            ],
        ),
        migrations.CreateModel(
            name='StoreMapping',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('merchant_id', models.CharField(max_length=16, verbose_name='Merchant ID')),
                ('store', models.ForeignKey(to='stores.Store')),
            ],
        ),
        migrations.AddField(
            model_name='articlemapping',
            name='product',
            field=models.ForeignKey(to='stores.Product'),
        ),
    ]
