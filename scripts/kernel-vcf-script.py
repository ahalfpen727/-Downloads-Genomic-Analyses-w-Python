
# coding: utf-8

# ## Load Python libraries

# In[ ]:


import sys
import pprint
import pybedtools as pb 
import gffutils as gt
import matplotlib.pyplot as plt
import sys
sys.path


# In[3]:


pip install pandas


# In[5]:


import sys
sys.path
import numpy as np
import matplotlib.pylab as plt
import pandas as pd
import numpy as np


# In[ ]:


from pybedtools import genome_registry
from pygtftk.gtf_interface import GTF


# In[ ]:


from pybedtools import BedTool
grch38gff='/home/drew/Desktop/IPyNB-Variant-Analysis/data/cuffcmp.combined.gtf'
#snps = BedTool('snps.bed.gz')  # [1]
genes = BedTool(grch38gff)    # [1]


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'ln -P /home/drew/Desktop/IPyNB-Variant-Analysis/data\nln -P /media/drew/easystore/ReferenceGenomes/GCA_000001405.15_GRCh38_no_alt_analysis_set/\nln -P /media/drew/easystore/ReferenceGenomes/GRCh38/')


# In[ ]:


intergenic_snps = snps.subtract(genes)                       # [2]
nearby = genes.closest(intergenic_snps, d=True, stream=True) # [2, 3]

for gene in nearby:             # [4]
    if int(gene[-1]) < 5000:    # [4]
        print gene.name         # [4]


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'cd /media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2018_07\npwd\nls -l */*vcf')


# In[ ]:


get_ipython().run_cell_magic('bash', '/media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2018_07/2018_07.', "gsa2vcf = '/media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2020_01/2020_01.clinvar.GSA-24v2.vcf'\ndatadir='/home/drew/Desktop/IPyNB-Variant-Analysis/data'")


# In[ ]:


#filename = "2018_07.clinvar.GRCh38.GSA-24v1.vcf"
vcf_reader = vcf.Reader(open('/media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2018_07/2018_07.clinvar.GRCh38.GSA-24v1.vcf', 'r'))
vcf_reader
sample = vcf_reader.samples
print(sample)


# In[ ]:


vcf_reader = vcf.Reader(open('/media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2018_07/2018_07.clinvar.GRCh38.GSA-24v1.vcf', 'r'))
vcfcalls = al.read_vcf(vcffile)
vcfcalls['samples']


# In[ ]:


vcffile = '/media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2020_01/2020_01.clinvar.GSA-24v2.vcf'
vcfcalls = al.read_vcf(vcffile)
sorted(vcfcalls.keys())


# In[ ]:


vcffile = '/media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2018_07/2018_07.clinvar.GRCh38.GSA-24v1.vcf'
#bcf_in = VariantFile(vcffile)  # auto-detect input format
#print(bcf_in.header.samples,10)
callset = al.read_vcf(vcffile, fields='*')
sorted(callset.keys())
df = al.vcf_to_dataframe(vcffile)
df


# In[ ]:


get_ipython().run_cell_magic('bash', '', 'cd /media/drew/easystore/Current-Analysis/AnalysisBaseDir/GSA_Data/2020_01')


# In[ ]:


#=open('2018_07.GSA-24v1_0.GRCh38.vcf', mode='r')
gsavcf=read_vcf('2018_07.clinvar.GRCh38.GSA-24v1.vcf')

#filename = "2018_07.clinvar.GRCh38.GSA-24v1.vcf"
vcf_reader = vcf.Reader(open('/media/drew/easystore/GoodCell-Resources/AnalysisBaseDir/GSA_Data/2018_07/2018_07.clinvar.GRCh38.GSA-24v1.vcf', 'r'))
print(length(vcf_reader))

for rec in bcf_in.fetch('10', 10500000, 105500000):
    # Get the Genotype value for the sample, or 'None' if missing
    gt = rec.samples[sample].get('GT',None)

    print rec.chrom, rec.pos, rec.id, gt


# In[ ]:


home(/drew/Desktop/IPyNB-Variant-Analysis/data/isoform_exp.diff)


# In[ ]:



for rec in vcf_reader.fetch('10', 10500000, 105500000):
    gt = rec.genotype(sample)['GT']
    print(rec.CHROM, rec.POS, rec.ID, rec.REF, gt)


# In[ ]:


# Generate random numbers simulating gene-expression values
geneA = normal(size=1000)
geneB = normal(size=1000)

# get_ipython().magic('matplotlib inline')
plt.plot(geneA, geneB, "o", color="#99C1C2")
plt.xlabel("Gene A")
plt.ylabel("Gene B")
plt.show()

