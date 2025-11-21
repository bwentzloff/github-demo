#!/usr/bin/env python3

from pathlib import Path

def gc_content(seq):
    seq = seq.upper()
    gc = seq.count("G") + seq.count("C")
    return round((gc / len(seq)) * 100, 2)

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

    rows = []
    for name, seq in read_fasta(fasta_path):
        gc = gc_content(seq)
        rows.append((name, gc))

    with open(output_path, "w") as out:
        out.write("seq_id\tgc_percent\n")
        for name, gc in rows:
            out.write(f"{name}\t{gc}\n")

    print(f"Wrote GC results to {output_path}")

if __name__ == "__main__":
    main()
