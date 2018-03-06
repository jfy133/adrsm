#!/usr/bin/env python

from numpy import random as npr
import matplotlib.pyplot as plt
import lib.adrsmlib as ad

import argparse

def _get_args():
    '''This function parses and return arguments passed in'''
    parser = argparse.ArgumentParser(
    prog='MetaBenReadSim',
    description='Metagenomic Benchmarking Read Simulator for ancient DNA')
    parser.add_argument('infile', help="path to reference fasta file")
    parser.add_argument(
    '-n',
    dest="nbReads"
    default=1000,
    help="Number of reads to simulate. Default = 1000")
    parser.add_argument(
    '-c',
    dest='coverage',
    default=None,
    help="Coverage - Replaces the number of reads if set. Default = None")
    parser.add_argument(
    '-r',
    dest='readLength',
    default=76,
    help="Average read length. Default = 76")
    parser.add_argument(
    '-i',
    dest='insertLength',
    default=47,
    help="Average insert length. Default = 47")
    parser.add_argument(
    '-l',
    dest="lenStdev"
    default=10,
    help="Insert length standard deviation. Default = 10")
    parser.add_argument(
    '-fwd',
    dest="fwdAdapt",
    default="AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG",
    help="Forward adaptor. Default = AGATCGGAAGAGCACACGTCTGAACTCCAGTCACNNNNNNATCTCGTATGCCGTCTTCTGCTTG")
    parser.add_argument(
    '-rev',
    dest="revAdapt",
    default="AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT",
    help="Reverse adaptor. Default = AGATCGGAAGAGCGTCGTGTAGGGAAAGAGTGTAGATCTCGGTGGTCGCCGTATCATT")
    parser.add_argument(
    '-e',
    dest="error",
    default=0.01,
    help="Illumina sequecing error. Default = 0.01")
    parser.add_argument(
    '-o',
    dest="output",
    default=None,
    help="Output file basename. Default = ./{basename}.*")

    args = parser.parse_args()

    infile = args.infile
    nread = int(args.nbReads)
    coverage = float(args.coverage)
    readlen = int(args.readLength)
    inserlen = int(args.insertLength)
    lendev = int(args.lenStdev)
    a1 = args.fwdAdapt
    a2 = args.revAdapt
    err = float(args.error)
    outfile= args.output

    return(infile, nread, coverage, readlen, inserlen, lendev, a1, a2, err, outfile)

if __name__ == "__main__":
    INFILE, NREAD, COV, READLEN, INSERLEN, LENDEV, A1, A2, ERR, OUTFILE = _get_args()
    MINLENGTH = 20

    ad.run_read_simulation(INFILE, NREAD, READLEN, INSERLEN, LENDEV, A1, A2, OUTFILE, MINLENGTH, ERR)
