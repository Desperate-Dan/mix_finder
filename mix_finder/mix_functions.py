#!/usr/bin/env python3

# import some bits

import os
import sys
import argparse
import re

from Bio import SeqIO

# first function to parse the input fasta files and look for Ns.
def fasta_reader(input_fasta):
  for record in SeqIO.parse(input_fasta, "fasta"):        
    N_bases = re.finditer("[AGCT][^ACGT]{1,3}[AGCT]", str(record.seq))
    coord_list = []
    for mo in N_bases:
        N_coord = mo.start()
        coord_list.append(N_coord)
        print(coord_list)
    seq_dict[record.id] = coord_list  

print(seq_dict)
