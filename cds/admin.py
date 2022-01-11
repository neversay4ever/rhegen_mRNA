from django.contrib import admin
from .models import Record, Protein, Codon, Triplet
# Register your models here.


class RecordAdmin(admin.ModelAdmin):
    model = Record
    list_display = [field.name for field in Record._meta.get_fields()
                    if field.name != 'id']


class ProteinAdmin(admin.ModelAdmin):
    model = Protein
    list_display = [field.name for field in Protein._meta.get_fields()
                    if field.name != 'id']


class CodonAdmin(admin.ModelAdmin):
    model = Codon
    list_display = [field.name for field in Codon._meta.get_fields()
                    if field.name != 'id']


class TripletAdmin(admin.ModelAdmin):
    model = Triplet
    list_display = [field.name for field in Triplet._meta.get_fields()
                    if field.name != 'id']


admin.site.register(Record, RecordAdmin)
admin.site.register(Protein, ProteinAdmin)
admin.site.register(Codon, CodonAdmin)
admin.site.register(Triplet, TripletAdmin)
