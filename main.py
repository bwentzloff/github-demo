#!/usr/bin/env python3

from pathlib import Path

def count_motif(seq, motif):
    return seq.upper().count(motif.upper())

def read_fasta(path):
    with open(path) as f:
        name = None
        seq_lines = []
        for line in f:
            line = line.strip()
            if line.startswith(">"):
                if name is not None:
                    yield name, "".join(seq_lines)
                name = line[1:]
                seq_lines = []
            else:
                seq_lines.append(line)
        if name is not None:
            yield name, "".join(seq_lines)

def main():
    fasta_path = Path("sequences.fasta")
    output_path = Path("output.tsv")

    motif = "TA"

    rows = []
    for name, seq in read_fasta(fasta_path):
        n_motif = count_motif(seq, motif)
        rows.append((name, n_motif))

    with open(output_path, "w") as out:
        out.write("seq_id\tcg_motif_count\n")
        for name, n_motif in rows:
            out.write(f"{name}\t{n_motif}\n")

    print(f"Wrote updated results to {output_path}")

if __name__ == "__main__":
    main()
