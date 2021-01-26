#!/bin/bash

#SBATCH -p hpc-bio-ochoa
#SBATCH --chdir=/home/alumno19/lab3-container/singularity
#SBATCH -J lab3_cvg
#SBATCH --cpus-per-task=1
#SBATCH --mail-type=END   # END/START/NONE
#SBATCH --mail-user=crivalgon@gmail.com

module load singularity/3.7.0

python3.6 ../extra/vecinas_test.py
singularity exec python_latest.sif python ../extra/vecinas_test.py


