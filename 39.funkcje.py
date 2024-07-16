# -*- coding: utf-8 -*-
import math 

# %%
def  GiveGeomSeqElement(a1 = 2, factor = 2, index = 2):
    # funkcja liczy ciag geometryczny
    print('element :', a1 * factor ** (index - 1))
    
# %%
GiveGeomSeqElement(1, 2, 64)

# %%
a1 = 3
factor = 2
maxindex = 10

# %%
for elementy in range(10):
    an = GiveGeomSeqElement(a1=a1,factor=factor,index=elementy)
    print(elementy, '=', an)

# %%
def GiveFactorForGeomSeq(term, nextterm):
    # funkcja wyznaczy wartość współczynnika gdy znane są 2 kolejne wyrazy ciągu.
    print('wynik :', nextterm / term)
    
GiveFactorForGeomSeq(12, 24)

# %%
def GiveSumOfNElementsGeomSeq(a1 = 2, factor = 2, n = 2):
    print('wynik:', a1 * (1 - factor ** n) / (1 - factor))
    
GiveSumOfNElementsGeomSeq(2, 3, 4)


    

