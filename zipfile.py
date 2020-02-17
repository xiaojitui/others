#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import tarfile
import gzip
import numpy as np 
from io import StringIO, BytesIO 
import base64
import os
import pandas as pd
from tqdm import tqdm


# In[ ]:





# In[ ]:


tar = tarfile.open('testfile.tsv.gz', 'r:gz') 
members = tar.getmembers()


# In[ ]:





# In[ ]:


for member in tqdm(members, total = len(members)):
    f = tar.extractfile(member)
    binaryfile = f.read()
    data = binaryfile.decode('utf8').encode('utf-8')
    df = pd.read_csv(BytesIO(data), encoding='utf-8')
    filename = os.path.join('./dataresults/', member.name)
    df.to_csv(filename, index_label = False, index = False)


# In[ ]:





# In[ ]:





# In[ ]:


saveimgs = []
#files = os.listdir(savepath)
for file in files:
    imgfile = os.path.join(path, file)
    saveimgs.append(imgfile)

import zipfile 
with zipfile.ZipFile('./imgchart.zip', 'w') as myzip:
    for f in saveimgs:  
        myzip.write(f)


# In[ ]:





# In[ ]:


filename = 'x.zip'
outputfile = '/myfolder/'
from zipfile import ZipFile
with ZipFile(filename, 'r') as f:
    allnames = f.namelist()
    for name in allnames:
        if name.endswith('.csv'):
            f.extract(name, outputfile)


# In[ ]:




import os
import zipfile

def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            ziph.write(os.path.join(root, file))

if __name__ == '__main__':
    zipf = zipfile.ZipFile('Python.zip', 'w', zipfile.ZIP_DEFLATED)
    zipdir('tmp/', zipf)
    zipf.close()
    
    
    
import shutil
shutil.make_archive(output_filename, 'zip', dir_name)
