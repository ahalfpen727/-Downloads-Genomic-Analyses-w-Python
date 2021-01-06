
# coding: utf-8

# ## Load Python libraries

# In[1]:


get_ipython().magic('matplotlib inline')

import matplotlib.pyplot as plt
from numpy.random import normal


# ## Generate random numbers simulating gene-expression values

# In[2]:


geneA = normal(size=1000)
geneB = normal(size=1000)


# ## Plot the values

# In[3]:


plt.plot(geneA, geneB, "o", color="#99C1C2")
plt.xlabel("Gene A")
plt.ylabel("Gene B")
plt.show()


# In[13]:


import vcf as vcf
import allel as al
from pysam import VariantFile
from pprint import pprint


# In[14]:


get_ipython().run_cell_magic('bash', '', '#ln -s /media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data\u200b/2018_07/2020_01.GSA_24v1_0.vcf\n#ln -s /media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data\u200b/2020_01/2020_01.GSA_24v2_0.vcf')


# In[15]:


get_ipython().run_cell_magic('bash', '', 'cd /media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2018_07\npwd\nls')


# In[16]:


#=open('2018_07.GSA-24v1_0.GRCh38.vcf', mode='r')
gsavcf=al.read_vcf('2018_07.clinvar.GRCh38.GSA-24v1.vcf')


# In[4]:



for rec in vcf_reader.fetch('10', 10500000, 105500000):
    gt = rec.genotype(sample)['GT']
    print(rec.CHROM, rec.POS, rec.ID, rec.REF, gt)

