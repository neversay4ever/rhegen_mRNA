from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.


class UTR5(models.Model):
    utr5_id = models.CharField(_("UTR5编号"), max_length=50)
    utr5_note = models.CharField(_("UTR5备注"), max_length=100)
    utr5_seq = models.TextField(_("UTR序列"))
