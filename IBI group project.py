# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 09:12:02 2019

@author: jxm72
"""
from collections import Counter
dna=input('Please input a DNA sequence:')
DNA=list(dna)
count=Counter(DNA)#get the number of each type of nucleotide
L=len(dna)
print('The GC content is:',(count['G']+count['C'])*100/L,'%')

DNA1=cdna=mRNA=DNA[::]
nuc=['A','G','C','T']
pair=['T','C','G','A']
mrna=['U','C','G','A']

def basepair(x1,x2):
    for i in range(len(nuc)):
        for j in range(len(DNA1)):
            if DNA1[j] in nuc[i]:
                x1[j]=x2[i] 
    return x1
#complementary dna
a=basepair(cdna,pair)        
print('The complementary DNA sequence is:',''.join(a[::-1]))

#mrna
b=basepair(mRNA,mrna) 
mRNA=''.join(mRNA)      
print('The mRNA sequence is:',mRNA)

#mrna to protein
codon={"UUU":"F", "UUC":"F", "UUA":"L", "UUG":"L","UCU":"S", "UCC":"s", "UCA":"S", "UCG":"S",
    "UAU":"Y", "UAC":"Y", "UGU":"C", "UGC":"C", "UGG":"W", "CUU":"L", "CUC":"L", "CUA":"L", 
    "CUG":"L","CCU":"P", "CCC":"P", "CCA":"P", "CCG":"P", "CAU":"H", "CAC":"H", "CAA":"Q", 
    "CAG":"Q","CGU":"R", "CGC":"R", "CGA":"R", "CGG":"R", "AUU":"I", "AUC":"I", "AUA":"I", 
    "AUG":"M","ACU":"T", "ACC":"T", "ACA":"T", "ACG":"T", "AAU":"N", "AAC":"N", "AAA":"K", 
    "AAG":"K","AGU":"S", "AGC":"S", "AGA":"R", "AGG":"R", "GUU":"V", "GUC":"V", "GUA":"V", 
    "GUG":"V","GCU":"A", "GCC":"A", "GCA":"A", "GCG":"A", "GAU":"D", "GAC":"D", "GAA":"E", 
    "GAG":"E","GGU":"G", "GGC":"G", "GGA":"G", "GGG":"G",}
if 'AUG' in mRNA:
    mRNA1=mRNA.split('AUG')[1]
    lmrna=[mRNA1[i:i+3] for i in range(0,len(mRNA1),3)]
    protein=['']*len(lmrna)
    k=list(codon.keys())
    v=list(codon.values())
    for i in range(len(k)):
        for j in range(len(lmrna)):
            if lmrna[j] in ['UAA','UAG','UGA']:
                break
            elif lmrna[j] in k[i]:
                protein[j]=v[i] 
    print('The polypeptide sequence is:', ''.join(protein))
else:
    print('This DNA sequence does not encode protein!')
