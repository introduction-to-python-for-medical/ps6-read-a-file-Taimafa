def create_codon_dict(file_path):
    path="data/codons.txt"
    file = open(path)
    rows = file.readlines()
    file.close()
    mapping={}
    for row in rows:
      cells=row.strip().split('\t')
      codon=cells[0]
      amino_acid=cells[2]
      mapping[codon]=amino_acid
    return mapping


