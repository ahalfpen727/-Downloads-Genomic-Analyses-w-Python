#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 10:20:20 2020

@author: drew
"""


# The name of the first sample in this VCF file
sample = bcf_in.header.samples[0]
# The name of the first sample in this VCF file
sample = vcf_reader.samples[0]

for rec in vcf_reader.fetch('10', 10500000, 105500000):
    gt = rec.genotype(sample)['GT']
    print(rec.CHROM, rec.POS, rec.ID, rec.REF, gt)
    
for rec in bcf_in.fetch('10', 10500000, 105500000):
    # Get the Genotype value for the sample, or 'None' if missing
    gt = rec.samples[sample].get('GT',None)

    print(rec.chrom, rec.pos, rec.id, gt)


vcf_reader = vcf.Reader(open(filename, 'r'))

