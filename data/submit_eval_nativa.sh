#!/bin/bash

#SBATCH -p hpc-bio-ochoa
#SBATCH --chdir=/home/alumno19/lab3-container/data
#SBATCH -J lab3_cvg
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END   # END/START/NONE
#SBATCH --mail-user=crivalgon@gmail.com


# En c++:

time ./k-mer13

time ./k-mer14

# En python:

time python3.6 k-mer13.py
time python3.6 k-mer14.py
