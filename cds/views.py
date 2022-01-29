from django.shortcuts import render
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from .models import Record, Protein, Codon, Triplet

# Create your views here.
from CAI import CAI
import random
from dnachisel import *
import RNA

def codon_optimize(request):
    gfp = Protein.objects.get(gene_name='GFP')
    gfp_aa = list(gfp.gene_aa_seq)
    gfp_refseq = gfp.gene_default_seq
    word_each_line = 30
    lines = len(gfp_aa)//word_each_line
    remainder = len(gfp_aa) % word_each_line
    data = []
    for i in range(0, len(gfp_aa)):
        codon = Codon.objects.get(aa_abbr=gfp_aa[i])
        dna = codon.aa_dna.split(",")
        data.append([codon.aa_abbr, codon.aa_color, dna])
    # 通过数据库把序列的信息全部挂上
    # 把序列转换成objects
    # 使用html的data-属性
    # javascript访问时直接用 (element).dataset.(data后面的字符)，如data-column="3", var article = document.querySelector('#electriccars'); article.dataset.columns // "3"
    codons = Codon.objects.all()
    triplets = Triplet.objects.all()

    context = {
        'gfp_aa': gfp_aa,
        'codons': codons,
        'triplets': triplets,
        'data': data,
        'gfp_refseq':gfp_refseq,
    }
    return render(request, 'cds/codon.html', context)


def get_seq(request):
    context = {}
    seq = ''
    if request.method == 'POST':
        for key in request.POST:
            if key != 'csrfmiddlewaretoken':
                seq += request.POST.get(key).strip()
    gfp = Protein.objects.get(gene_name='GFP')
    gfp_refseq = gfp.gene_default_seq
    cai_score = CAI(seq, reference=[gfp_refseq])
    cai_score = round(cai_score, 3)
    gc_count = 0
    for i in list(seq):
        i = i.upper()
        if i == 'C' or i=="G":
            gc_count +=1
    gc_ratio = round(gc_count/len(seq),3)
    pair_seq = RNA.fold(seq)
    print(pair_seq[0])
    pair_seq[0] = ''.join(pair_seq[0])
    print(pair_seq[0])
    context = {
        'seq': seq,
        'good': 'sfgsf',
        'cai_score': cai_score,
        'gc_ratio': gc_ratio,
        'pair_seq':pair_seq[0],
        'mfe':round(pair_seq[1],3),
        'type':'get_seq',
    }
    return render(request, 'cds/seq.html', context)

def eq_random_seq(request):
    gfp = Protein.objects.get(gene_name='GFP')
    gfp_aa = list(gfp.gene_aa_seq)
    seq =''
    for i in range(0, len(gfp_aa)):
        codon = Codon.objects.get(aa_abbr=gfp_aa[i])
        dna = codon.aa_dna.split(",")
        dna_ratio = codon.aa_ratio.split(",")
        dna_choice = random.choices(dna,  k=1)
        seq +=dna_choice[0].strip()
    seq = ''.join(seq)
    gfp_refseq = gfp.gene_default_seq
    cai_score = 0
    cai_score = CAI(seq, reference=[gfp_refseq])
    cai_score = round(cai_score, 3)
    gc_count = 0
    for i in list(seq):
        i = i.upper()
        if i == 'C' or i=="G":
            gc_count +=1
    gc_ratio = round(gc_count/len(seq),3)
    
    pair_seq = RNA.fold(seq)

    context = {
        'seq': seq,
        'cai_score': cai_score,
        'gc_ratio': gc_ratio,
        'pair_seq':pair_seq[0],
        'mfe':round(pair_seq[1],3),
        'type': 'eq_random_seq',
    }
    return render(request, 'cds/seq.html', context)


def prob_random_seq(request):
    gfp = Protein.objects.get(gene_name='GFP')
    gfp_aa = list(gfp.gene_aa_seq)
    seq =''
    for i in range(0, len(gfp_aa)):
        codon = Codon.objects.get(aa_abbr=gfp_aa[i])
        dna = codon.aa_dna.split(",")
        dna_ratio = codon.aa_ratio.split(",")
        dna_ratio = [int(float(i)*100) for i in dna_ratio]
        print(dna_ratio)
        dna_choice = random.choices(dna, weights=dna_ratio, k=1)
        seq +=dna_choice[0].strip()
    seq = ''.join(seq)
    gfp_refseq = gfp.gene_default_seq
    cai_score = 0
    cai_score = CAI(seq, reference=[gfp_refseq])
    cai_score = round(cai_score, 3)
    gc_count = 0
    for i in list(seq):
        i = i.upper()
        if i == 'C' or i=="G":
            gc_count +=1
    gc_ratio = round(gc_count/len(seq),3)
    
    pair_seq = RNA.fold(seq)
    context = {
        'seq': seq,
        'cai_score': cai_score,
        'gc_ratio': gc_ratio,
        'pair_seq':pair_seq[0],
        'mfe':round(pair_seq[1],3),
        'type':'prob_random_seq',
    }
    return render(request, 'cds/seq.html', context)


def dnachisel_seq(request):
    gfp = Protein.objects.get(gene_name='GFP')
    gfp_refseq = gfp.gene_default_seq

    problem = DnaOptimizationProblem(
        sequence=gfp_refseq,
        constraints=[
            AvoidPattern("BspQI_site"),
            EnforceGCContent(mini=0.3, maxi=0.7, window=50),
        ],
        objectives=[CodonOptimize(species='h_sapiens')]
    )
    # SOLVE THE CONSTRAINTS, OPTIMIZE WITH RESPECT TO THE OBJECTIVE

    problem.resolve_constraints()
    problem.optimize()

    # PRINT SUMMARIES TO CHECK THAT CONSTRAINTS PASS
    print(problem.constraints_text_summary())
    print(problem.objectives_text_summary())

    # GET THE FINAL SEQUENCE (AS STRING OR ANNOTATED BIOPYTHON RECORDS)

    dnachisel_sequence = problem.sequence  # string

    cai_score = 0
    cai_score = CAI(dnachisel_sequence, reference=[gfp_refseq])
    cai_score = round(cai_score, 3)
    gc_count = 0
    for i in list(dnachisel_sequence):
        i = i.upper()
        if i == 'C' or i=="G":
            gc_count +=1
    gc_ratio = round(gc_count/len(dnachisel_sequence),3)
    
    pair_seq = RNA.fold(dnachisel_sequence)
    context = {
        'seq': dnachisel_sequence,
        'cai_score': cai_score,
        'gc_ratio': gc_ratio,
        'pair_seq':pair_seq[0],
        'mfe':round(pair_seq[1],3),
        'type':'dnachisel_seq',
    }
    return render(request, 'cds/seq.html', context)