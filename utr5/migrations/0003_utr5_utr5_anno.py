# Generated by Django 3.2 on 2022-01-27 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utr5', '0002_auto_20220111_1402'),
    ]

    operations = [
        migrations.AddField(
            model_name='utr5',
            name='utr5_anno',
            field=models.JSONField(null=True, verbose_name='UTR5注释motif'),
        ),
    ]
