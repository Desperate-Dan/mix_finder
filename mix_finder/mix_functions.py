#!/usr/bin/env python3

# import some bits

import os
import sys
import argparse
import re

from Bio import SeqIO


# define the arguments for the command
def get_arguments(sysargs = sys.argv[1:]):
    '''
    Parse the command line arguments.
    '''
    parser = argparse.ArgumentParser(description='Scans fasta files for small groups of ambiuous bases and then sticks coordinates into bammix')

    main_group = parser.add_argument_group('Main options')
    main_group.add_argument('-f', '--fasta', dest='input_fasta', required=True,
                            help='Path to directory of consensus fastas')
    main_group.add_argument('-b', '--bam', dest='input_bam', default=None,
                            help='Path to the folder containing the appropriate bam and index files')
    main_group.add_argument('-m', '--window-max', dest='max', default=3,
                            help='Max size for ambiguous window (default = 3)')
    main_group.add_argument('-n', '--window-min', dest='min', default=1,
                            help='Min size for ambiguous window (default = 1)')

    if len(sysargs)<1:
        parser.print_help()
        sys.exit(-1)
    else:
        args = parser.parse_args(sysargs)


    # first function to parse the input fasta files and look for non-AGCTs.
    def ambig_base_finder(input_fasta,min=1,max=3):
        seq_dict = {}
        for record in SeqIO.parse(input_fasta, "fasta"):
            N_bases = re.finditer("[AGCT][^AGCT]{" + str(min) + "," + str(max) + "}[AGCT]", str(record.seq))
            coord_list = []
            for mo in N_bases:
                start_coord = mo.start()
                end_coord = mo.end()
                start_coord += 1
                while start_coord != (end_coord - 1):
                    coord_list.append(start_coord)
                    start_coord += 1
                    print(coord_list)


            seq_dict[record.id] = coord_list
        print(seq_dict)
        return(seq_dict)

    

    ambig_base_finder(args.input_fasta,args.min,args.max)

get_arguments()
