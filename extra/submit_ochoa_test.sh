#!/bin/bash

#SBATCH -p hpc-bio-ochoa
#SBATCH --chdir=/home/alumno19/lab3-container/extra
#SBATCH -J lab3_cvg
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END   # END/START/NONE
#SBATCH --mail-user=crivalgon@gmail.com

module load singularity/3.7.0

python3.6 vecinas_test.py
singularity exec ../singularity/python_latest.sif python vecinas_test.py


