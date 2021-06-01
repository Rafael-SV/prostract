import subprocess
import os
import sys
import pdbfixer
import simtk
from simtk.openmm.app import PDBFile

"""
psuedocode overview:
    import pdb
    count chains
    remove all but first chain
    find missing residues
        add missing residue dict to list to writeout later
    add missing atoms
    writeout file (PDB format?) with new metadata about which atoms were missing
repeat
"""

def remove_extra_chains(pdbfixer_obj):
    num_chains = sum(1 for i in pdbfixer_obj.topology.chains())
    pdbfixer_obj.removeChains(range(1, num_chains))
    return pdbfixer_obj

def add_missing_atoms(pdbfixer_obj):
    pdbfixer_obj.findMissingResidues()
    pdbfixer_obj.findMissingAtoms()
    pdbfixer_obj.addMissingAtoms()
    return pdbfixer_obj

# collect pdb file names in list
directory_content = []

scndr_obj = os.scandir('../pdb_files')
for item in scndr_obj :
    pdb = item.name
    directory_content.append(pdb)
print(directory_content)
scndr_obj.close()

#read the list of pdb file names, add atoms, add added atom count to dict with pdb name as key
missing_atom_dict = {}

for pdb_name in directory_content:
    file_path = '../pdb_files/' + pdb_name
    fix_pdb = pdbfixer.PDBFixer(filename=file_path)
    fix_pdb = remove_extra_chains(fix_pdb)
    fix_pdb = add_missing_atoms(fix_pdb)
    number_missing_atoms = sum(1 for i in fix_pdb.missingAtoms())
    missing_atom_dict[pdb_file_path] = number_missing_atoms
    output_file_name = str('fixed_' + pdb_file_path)
    with open(output_file_name, 'w') as output_pdb:
        fix_pdb.writeFile(fix_pdb.topology, fix_pdb.positions, output_pdb)
with open('pdb_name_and_number_missing_atoms_dict.pkl', 'w') as f:
    pickle.dump(missing_atom_dict, f)


