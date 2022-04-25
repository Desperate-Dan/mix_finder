#!/usr/bin/env python3

# import some bits

import os
import sys
import argparse
import re

from Bio import SeqIO

# first function to parse the input fasta files and look for non-AGCTs.
def ambig_base_finder(input_fasta,min=1,max=3):
  seq_dict = {}
  for record in SeqIO.parse(input_fasta, "fasta"):        
    N_bases = re.finditer("[AGCT][^AGCT]{" + str(min) + "," + str(max) + "}[AGCT]", str(record.seq))
    coord_list = []
    for mo in N_bases:
        N_coord = mo.start()
        coord_list.append(N_coord)
        print(coord_list)
    seq_dict[record.id] = coord_list
  return(seq_dict)

