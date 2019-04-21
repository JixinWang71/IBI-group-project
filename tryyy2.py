# -*- coding: utf-8 -*-
"""
Created on Sun Apr 21 21:58:07 2019

@author: jxm72
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:44:41 2019

@author: jxm72
"""
import sys
import re
import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
seq='TCGAGGGATCCAATTCGAATTCAAGCTTACGTAGCTGGATCCGGATCCGGATCC'
seql=list(seq)

diction={'AluI':['(TCGA)|(AGCT)','AGCT',2],'HindIII':['(AAGCTT)|(TTCGAA)','AAGCTT',1],'BamHI':['(GGATCC)|(CCTAGG)','GGATCC',1],'SalI':['(GTCGAC)|(CAGCTG)','GTCGAC',1]}
keys=list(diction.keys())
values=list(diction.values())


def location(seq,enzyme):
    index=keys.index(enzyme)
    fragment=[]
    loc=[]
    loca=set()
    rex=re.compile(values[index][0])
    for i in range(len(seq)-len(values[index][1])):
        fragment.append(seq[i:i+len(values[index][1])])
        for j in range(len(fragment)):
            if rex.search(fragment[j]):
                loc.append(j)
                loca=set(loc)
    return loca
                    

def digest(seql,location,enzyme):
    index=keys.index(enzyme)
    number=values[index][2]
    
    for i in location:
        seql.insert(i+number,'?')
    seq=str(''.join(seql))
    fragment=seq.split('?')
    return fragment
    
for i in keys:
    #print(location)
    seql=list(seq)
    
    locati=location(seq,i)
    fragment=digest(seql,locati,i)
    print(i,fragment)
    y_pos = np.arange(len(fragment))
    performance = [len(i) for i in fragment] 
    plt.bar(y_pos, performance, )
    plt.xticks(y_pos)
    plt.ylabel('bp')
    plt.title('DNA fragments')
     
    plt.show()   

 
    #diction={'AluI':['(?=(?P<AluI>AGCT))','AGCT',2],'HindIII':['(?=(?P<HindIII>AAGCTT))','AAGCTT',1],'BamHI':['GGATCC','GGATCC',1],'SalI':['(?=(?P<SalI>GTCGAC))','GTCGAC',1]}
