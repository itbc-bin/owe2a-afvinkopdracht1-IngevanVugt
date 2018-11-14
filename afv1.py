# Naam: Inge van Vugt
# Datum: 14-11-18
# Versie: 2.0

# Opmerking: Het alpaca bestand is erg groot! Neem eerst een klein proefstukje van het bestand,
# met 5 tot 10 fasta's. Ga je runnen met het echte bestand,
# geef je programma dan even de tijd.


def main():
    try:
        bestand = "GCF_000164845.2_Vicugna_pacos-2.0.2_rna (1).fna"
        headers, seqs = lees_inhoud(bestand)
        zoekwoord = input("Geef een zoekwoord op: ")
        for i in range(len(headers)):
            if zoekwoord in headers[i]:
                print("Header:", headers[i])
                check_is_dna = is_dna(seqs[i])
                if check_is_dna:
                    print("Sequentie is DNA")
                    knipt(seqs[i])
                else:
                    print("Sequentie is geen DNA. Er is iets fout gegaan.")
    except FileNotFoundError:
        print("Het bestand bestaat niet")
    except IOError:
        print("Bestand kan niet geopend worden")


def lees_inhoud(bestands_naam):
    try:
        bestand = open(bestands_naam)
        headers = []
        seqs = []
        seq = ""
        for line in bestand:
            line = line.strip()
            if ">" in line:
                if seq != "":
                    seqs.append(seq)
                    seq = ""
                headers.append(line)
            else:
                seq += line.strip()
        seqs.append(seq)
        return headers, seqs
    except FileNotFoundError:
        print("Het bestand bestaat niet")
    except IOError:
        print("Bestand kan niet geopend worden")
    except TypeError:
        print("Q")

    
def is_dna(seq):
    dna = False
    a = seq.count("A")
    t = seq.count("T")
    c = seq.count("C")
    g = seq.count("G")
    total = a+t+c+g
    if total == len(seq):
        dna = True
    return dna


def knipt(alpaca_seq):
    try:
        bestand = open("enzymen.txt")
        for line in bestand:
            naam, seq = line.split(" ")
            seq = seq.strip().replace("^", "")
            if seq in alpaca_seq:
                print(naam, "knipt in sequentie")
    except FileNotFoundError:
        print("Het bestand niet")
    except IOError:
        print("Bestand kan niet geopend worden")

main()
