from Bio import Entrez, SeqIO
from Bio.Align import PairwiseAligner

# mail
Entrez.email = "a.falkowski.ptmr@gmail.com"

# Identyfikatory 
ids = ["JX669568", "JX669571"]

# Pobranie sekwencji z GenBank
handle = Entrez.efetch(
    db="nucleotide",
    id=ids,
    rettype="fasta",
    retmode="text"
)

records = list(SeqIO.parse(handle, "fasta"))
handle.close()

# Zapis do  FASTA
SeqIO.write(records, "sekwencje_genbank.fasta", "fasta")

print("Pobrano i zapisano sek. do pliku sekwencje_genbank.fasta")

# Wczytanie sekwencji z FASTA
wczytane = list(SeqIO.parse("sekwencje_genbank.fasta", "fasta"))

seq1 = str(wczytane[0].seq)
seq2 = str(wczytane[1].seq)

print("\nWczytane sek.:")
print(wczytane[0].id, "dlugosc:", len(seq1))
print(wczytane[1].id, "dlugosc:", len(seq2))

# Algorytm Needleman-Wunsch - dopasowanie 
aligner = PairwiseAligner()
aligner.mode = "global"

aligner.match_score = 1
aligner.mismatch_score = -1
aligner.open_gap_score = -2
aligner.extend_gap_score = -0.5

alignments = aligner.align(seq1, seq2)

best_alignment = alignments[0]

print("\nNajlepsze dopasowanie glob.:")
print(best_alignment)

print("\nPunktacja najlepszego dopasowania:")
print(best_alignment.score)