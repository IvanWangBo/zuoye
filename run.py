# -*- coding: utf-8 -*-

from TF_IDF import GrobalParament
from TF_IDF.prepro_file import prepro_file 
from TF_IDF.TF_IDF_Compute import TF_IDF_Compute
def Preprocess(file_url):
    PreResUrl=GrobalParament.PreprocessResultDir+'/'+GrobalParament.PreprocessResultName
    prepro_file(file_url,PreResUrl)
def TF_IDF(*words):
    PreResUrl=GrobalParament.PreprocessResultDir+'/'+GrobalParament.PreprocessResultName
    ResFileUrl=GrobalParament.ResultFileNameDir+'/'+GrobalParament.ResultFileName
    if GrobalParament.out_to_file:
        result = TF_IDF_Compute(PreResUrl,ResFileUrl,*words)
        return result
    else:
        result=TF_IDF_Compute(PreResUrl,ResFileUrl,*words)
        return result
    
#Preprocess('./news')
"""key = raw_input()
result = TF_IDF(key)
for r in result:
    for n in r:
        print n
"""