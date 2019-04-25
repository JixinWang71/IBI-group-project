from collections import Counter
dna=input('Please input a DNA sequence:')
DNA=list(dna)

def countgc(DNA):
    count=Counter(DNA)#get the number of each type of nucleotide
    L=len(DNA)
    print('The GC content is:',(count['G']+count['C'])*100/L,'%')

nuc=['A','G','C','T']
pair=['T','C','G','A']
mrna=['U','C','G','A']

def basepair(x2):
    x1=DNA[::]
    for i in range(len(nuc)):
        for j in range(len(DNA)):
            if DNA[j] == nuc[i]:
                x1[j]=x2[i] 
    return x1
#complementary dna
a=basepair(pair)        
print('The complementary DNA sequence is:',''.join(a[::-1]))

#mrna
b=basepair(mrna) 
mRNA=''.join(b)      
print('The mRNA sequence is:',mRNA)

#mrna to protein
file=open('codon.txt','r')
codon=eval(file.read())
if 'AUG' in mRNA:   
    location=mRNA.find('AUG')
    lmrna=[mRNA[i:i+3] for i in range(location,len(mRNA),3)]
    protein=['None']*len(lmrna)            
    k=list(codon.keys())
    v=list(codon.values())
    for i in range(len(k)):
        for j in range(len(lmrna)):
            if lmrna[j] in ['UAA','UAG','UGA']:
                break
            elif lmrna[j] == k[i]:
                protein[j]=v[i] 
    print('The polypeptide sequence is:', ''.join(protein))
else:
    print('This DNA sequence does not encode protein!')
file.close()




