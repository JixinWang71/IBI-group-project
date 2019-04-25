
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
#seq='TCGAGGGATCCAATTCGAATTCAAGCTTACGTAGCTGGATCCGGATCCGGATCCAAAAAGTCGACGCGCTTTCGCGATTTAGTCGTCGCAGCTAGTTTGCCAGAAGCGT'
#seq='AGCTTAAGCTTAAGCTTAAGCTTAAGCTTGGATCCGGATCCGTCGACGTCGAC'
#seq='AGCTGGGGGCT'
diction={'AluI':['AGCT',2],'HindIII':['AAGCTT',1],'BamHI':['GGATCC',1],'SalI':['GTCGAC',1]}#the distance to 5'
keys=list(diction.keys())
values=list(diction.values())

def digest(seql,location,enzyme):
    for i in location:
        seql.insert(i-1,'?')#insert ? befor i-1, that is exactly at the location of digestion    
    seq=str(''.join(seql))
    fragment=seq.split('?')
    return fragment

def location(seq,enzyme):
    index=keys.index(enzyme)
    number=values[index][1]
    length=len(values[index][0])
    fragment=[]#a list to store all the pieces of seq
    loc=[]#a list to store the location
    loca=set()
    rex=re.compile(values[index][0])    
    for i in range(len(seq)-length+1):
        fragment.append(seq[i:i+length])#split the seq according to the sequence length of restriction enzyme
    for j in range(len(fragment)):
        if rex.search(fragment[j]):
            loc.append(j+number+1)#get the index just before the location            
            loca=sorted(set(loc),reverse=True)#reverse the set so that when we insert the ?, the other won't be affected
    return loca
summary=[]    
for i in keys:  
    seql=list(seq)    
    loc=location(seq,i)
    if len(loc)==0:
        print("This DNA sequence can't be digested by",i )
    else:
        fragment=digest(seql,loc,i)
        summary.append(str(i)+':'+','.join(str(e) for e in loc))
        print(i,':',str(' / '.join(fragment)))
        #bar chart        
        fragments=(i+1 for i in range(len(fragment)))
        y_pos = np.arange(len(fragment))
        bplength = [len(i) for i in fragment] 
        plt.bar(y_pos, bplength)
        plt.xticks(y_pos,fragments)
        plt.ylabel('bp')
        plt.title('DNA fragments')     
        plt.show()   
print('The DNA is assumed to be linear. It can be digested by:')    
for e in summary:
    print(e)  
print('The number is the location of base (count from 1) after the restriction site')

