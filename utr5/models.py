from django.db import models
from django.utils.translation import ugettext_lazy as _
# Create your models here.
import json

class UTR5(models.Model):
    utr5_id = models.CharField(_("UTR5编号"), max_length=50)
    utr5_note = models.CharField(_("UTR5备注"), max_length=100)
    utr5_seq = models.TextField(_("UTR5序列"))
    utr5_anno = models.JSONField(_("UTR5注释motif"), null=True)
    
    @property
    def get_json_data(self):
        if self.utr5_anno is not None:
            return json.dumps(self.utr5_anno)
        else:
            return None
    class Meta:
        verbose_name_plural = "UTR5"
