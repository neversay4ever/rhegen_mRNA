codon_table = {
    'F': ['Phe', ['TTC', 'TTT'], [0.55, 0.45], [20.4, 16.9], '苯丙氨酸', '芳香族', 'slate'],
    'L': ['Leu', ['CTG', 'CTC', 'CTT', 'TTG', 'TTA', 'CTA'], [0.41, 0.20, 0.13, 0.13, 0.07, 0.07], [40.3, 19.4, 12.8, 12.6, 7.2, 6.9], '亮氨酸', '疏水', 'pink'],
    'Y': ['Tyr', ['TAC', 'TAT'], [0.57, 0.43], [15.6, 12.0], '酪氨酸', '芳香族', 'gray'],
    'H': ['His', ['CAC', 'CAT'], [0.59, 0.41], [14.9, 10.4], '组氨酸', '碱性', 'teal'],
    'Q': ['Gln', ['CAG', 'CAA'], [0.75, 0.25], [34.6, 11.8], '谷氨酰胺', '亲水', 'sky'],
    'I': ['Ile', ['ATC', 'ATT', 'ATA'], [0.48, 0.36, 0.16], [21.4, 15.7, 7.1], '异亮氨酸', '疏水', 'rose'],
    'M': ['Met', ['ATG'], [1.00], [22.3], '蛋氨酸', '疏水', 'red'],
    'N': ['Asn', ['AAC', 'AAT'], [0.54, 0.46], [19.5, 16.7], '天冬酰胺', '亲水', 'blue'],
    'K': ['Lys', ['AAG', 'AAA'], [0.58, 0.42], [32.9, 24.0], '赖氨酸', '碱性', 'cyan'],
    'V': ['Val', ['GTG', 'GTC', 'GTT', 'GTA'], [0.47, 0.24, 0.18, 0.11], [28.9, 14.6, 10.9, 7.0], '缬氨酸', '疏水', 'orange'],
    'D': ['Asp', ['GAC', 'GAT'], [0.54, 0.46], [26.0, 22.3], '天冬氨酸', '酸性', 'lime'],
    'E': ['Glu', ['GAG', 'GAA'], [0.58, 0.42], [40.8, 29.0], '谷氨酸', '酸性', 'green'],
    'S': ['Ser', ['AGC','TCC', 'TCT', 'AGT','TCA', 'TCG'], [0.24, 0.22, 0.18, 0.15, 0.15, 0.06], [19.4,17.4, 14.6, 11.9, 11.7, 4.5], '丝氨酸', '亲水', 'purple'],
    'C': ['Cys', ['TGC', 'TGT'], [0.55, 0.45], [12.2, 9.9], '半胱氨酸', '亲水', 'indigo'],
    'W': ['Trp', ['TGG'], [1.00], [12.8], '色氨酸', '芳香族', 'stone'],
    '*': ['Ter', ['TGA', 'TAA', 'TGG'], [0.52, 0.28, 0.20], [1.3, 0.7, 0.5], '终止', '无', 'black'],
    'P': ['Pro', ['CCC', 'CCT', 'CCA', 'CCG'], [0.33, 0.28, 0.27, 0.11], [20.0, 17.3, 16.7, 7.0], '脯氨酸', '疏水', 'amber'],
    'R': ['Arg', ['CGG', 'AGA', 'AGG', 'CGC', 'CGA', 'CGT'], [0.21, 0.20, 0.20, 0.19, 0.11, 0.08], [11.9, 11.5, 11.4, 10.9, 6.3, 4.7], '精氨酸', '碱性', 'emerald'],
    'T': ['Thr', ['ACC', 'ACA', 'ACT', 'ACG'], [0.36, 0.28, 0.24, 0.12], [19.2, 14.8, 12.8, 6.2], '苏氨酸', '亲水', 'violet'],
    'A': ['Ala', ['GCC', 'GCT', 'GCA', 'GCG'], [0.40, 0.26, 0.23, 0.11], [28.5, 18.6, 16.0, 7.6], '丙氨酸', '疏水', 'yellow'],
    'G': ['Gly', ['GGC', 'GGG', 'GGA', 'GGT'], [0.34, 0.25, 0.25, 0.16], [22.8, 16.4, 16.3, 10.8], '甘氨酸', '疏水', 'fuchsia'],
}
# # ①非极性、疏水性氨基酸：甘氨酸、丙氨酸、缬氨酸、亮氨酸、异亮氨酸、苯丙氨酸和脯氨酸。 9种。甲硫氨酸=蛋氨酸
# ②极性、中性氨基酸：色氨酸、丝氨酸、酪氨酸、半胱氨酸、蛋氨酸、天冬酰胺、谷氨酰胺和苏氨酸。7种。去掉  甲硫氨酸=蛋氨酸
# ③酸性的氨基酸：天冬氨酸和谷氨酸。
# ④碱性氨基酸：赖氨酸、精氨酸和组氨酸。
