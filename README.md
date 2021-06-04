# Protein structure abstraction for machine learning
## Proteins are complex polymers, with vast dimesionality
### This project aims to reduce the dimensionality of proteins to make machine learning tractable. 

This folder contains descriptive notebooks in ./notebooks (currently python code is in the notebooks, it will be added to ./src later) , every .PDB file from the RCSB protein databank in the ./pdb_files directory, external code repos (such as pdbfixer and openMM) in ./external

Currently the code to add fix missing atoms in PDB files runs too slowly. As written it will take 875 hours to process all 200,000 pdb files, on the available hardware. It needs to either incorporate multiprocessing or just be run on better machine.

Once the missing atoms are added, the data will be further processed into form suitable for graph neural network.
