#!/bin/bash

#SBATCH --job-name=minib21
#SBATCH --output=mini.out
#SBATCH --error=mini.err
#SBATCH --time=12:00:00
#SBATCH --partition=broadwl
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=28
#SBATCH --mem-per-cpu=2000
#SBATCH --constraint=fdr

# Load Python modules
module load python/anaconda-2020.02

python para_lowtol.py 