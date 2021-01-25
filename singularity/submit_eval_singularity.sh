#!/bin/bash

#SBATCH -p hpc-bio-ochoa
#SBATCH --chdir=/home/alumno19/lab3-container/singularity
#SBATCH -J lab3_cvg
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=NONE   # END/START/NONE
#SBATCH --mail-user=crivalgon@gmail.com

module load singularity/3.7.0

# En c++ desde el contenedor de Singularity: 

time singularity exec python_latest.sif ./k-mer13

time singularity exec python_latest.sif ./k-mer14

# En python:

time singularity exec python_latest.sif python ./k-mer13.py
time singularity exec python_latest.sif python ./k-mer14.py
