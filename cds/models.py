from django.db import models
from django.utils.translation import ugettext as _
# Create your models here.


class Record(models.Model):
    job_id = models.CharField(_("任务编号"), max_length=100, null=True, blank=True)
    aa_seq = models.TextField(_("氨基酸序列"), null=True, blank=True)
    dna_seq = models.TextField(_("DNA序列"))
    cai = models.FloatField(_("CAI值"), null=True, blank=True)
    gc = models.FloatField(_("GC含量"), null=True, blank=True)
    energy = models.FloatField(_("能量值"), null=True, blank=True)


class Protein(models.Model):
    gene_id = models.CharField(_("基因ID"), max_length=50)
    gene_name = models.CharField(_("基因名称"), max_length=50)
    gene_note = models.TextField(_("基因备注"))
    gene_aa_seq = models.TextField(_("氨基酸序列"))
    gene_default_seq = models.TextField(_("默认DNA序列"), null=True, blank=True)
    gene_optimize_seq = models.TextField(_("优化DNA序列"), null=True, blank=True)


class Codon(models.Model):
    aa_abbr = models.CharField(_("氨基酸缩写"), max_length=1)
    aa_name = models.CharField(_("氨基酸简称"), max_length=3)
    aa_cn = models.CharField(_("氨基酸中文"), max_length=20)
    aa_attr = models.CharField(_("氨基酸属性"), max_length=20)
    aa_color = models.CharField(_("颜色表示"), max_length=10)
    aa_dna = models.CharField(_("密码子"), max_length=100)
    aa_ratio = models.CharField(_("密码子比例"), max_length=100)
    aa_freq = models.CharField(_("密码子频率"), max_length=100)


class Triplet(models.Model):
    aa_dna = models.CharField(_("密码子"), max_length=3)
    aa_abbr = models.CharField(_("氨基酸缩写"), max_length=1)
    dna_ratio = models.FloatField(_("密码子比例"))
    dna_freq = models.FloatField(_("密码子频率"))
    dna_num = models.PositiveIntegerField(_("密码子数目"))
