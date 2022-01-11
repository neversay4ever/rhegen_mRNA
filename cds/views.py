from django.shortcuts import render
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Record, Protein, Codon, Triplet

# Create your views here.


def codon_optimize(request):
    gfp = Protein.objects.get(gene_name='GFP')
    gfp_aa = list(gfp.gene_aa_seq)
    word_each_line = 30
    lines = int(len(gfp_aa)/30)
    print(gfp_aa)
    print(len(gfp_aa))
    format_string = mark_safe('')
    for line in range(0, lines):
        format_string += mark_safe('<p>')
        for i in range(0, 30):
            index = line*30+i
            aa = gfp_aa[index]
            format_string += mark_safe('<span class=\"text-' +
                                       codon_table.get(aa)[-1]+'-700\">&nbsp;'+aa+'&nbsp;</span>')
        format_string += mark_safe('</p>')

    format_string += mark_safe('<p>')
    for aa_index in range(30*lines, len(gfp_aa)):
        aa = gfp_aa[aa_index]
        format_string += mark_safe('<span class=\"text-' +
                                   codon_table.get(aa)[-1]+'-700\">&nbsp;'+aa+'&nbsp;</span>')
    format_string += mark_safe('</p>')
    context = {
        'aa_print': format_string,
        'gfp_aa': gfp_aa,
        'codon': codon_table,
    }
    return render(request, 'cds/codon.html', context)
