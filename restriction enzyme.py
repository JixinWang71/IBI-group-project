# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 15:44:41 2019

@author: jxm72
"""
import Bio
from Bio import Restriction
from Bio.Restriction import *
from Bio.Seq import Seq
from Bio.Alphabet.IUPAC import IUPACAmbiguousDNA
from Bio.Restriction.Restriction_Dictionary import rest_dict, typedict
#print(rest_dict.values())
#print(Restriction.EcoRI)
#print(EcoRI)
#print(len(AllEnzymes))
alll=CommOnly
amb = IUPACAmbiguousDNA()
seq=Seq('AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAGGG', amb)
dic=alll.search(seq)
#print(alll.search(seq))
#print(dic.values())
lis=list(dic.values())
#print(lis)

j=0
for i in lis:
    if len(i)!=0:
        j=1
    if j==1:
        analong=Analysis(alll,seq,linear=True)
        #try1=analong.print_that()
        analong.print_as('map')
        analong.print_that()
        #analong.print_as('number')
        #analong.print_that()
        print(analong)
        break  
#print(EcoRI.search(seq))
#print(j)
if j==0:
    print('this dna sequence can not be digested by any restriction enzyme')
    

#print(alll[0])
