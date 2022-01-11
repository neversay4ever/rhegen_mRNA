# Generated by Django 3.2 on 2022-01-11 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cds', '0003_codontable'),
    ]

    operations = [
        migrations.CreateModel(
            name='Triplet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aa_dna', models.CharField(max_length=3, verbose_name='密码子')),
                ('aa_abbr', models.CharField(max_length=1, verbose_name='氨基酸缩写')),
                ('dna_ratio', models.FloatField(verbose_name='密码子比例')),
                ('dna_freq', models.FloatField(verbose_name='密码子频率')),
                ('dna_num', models.PositiveIntegerField(verbose_name='密码子数目')),
            ],
        ),
    ]