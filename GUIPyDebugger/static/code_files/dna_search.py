from enum import IntEnum
import timeit as t

# Input data
gene_str = "ACGTACTGCTGCATGTCGTATTATTCGGTACTGGCGCATGCTTTAAAGTACTGATCTAGAGCATGTCGTATTCAGGACTGATCGCATGCT"
Nucleotide = IntEnum("Nucleotide", ('A', 'C', 'G', 'T'))

# Functions
def string_to_gene(s):
    gene = []
    for i in range(0, len(s), 3):
        if (i + 2) >= len(s):
            return gene
        codon = (Nucleotide[s[i]], Nucleotide[s[i + 1]], Nucleotide[s[i + 2]])
        gene.append(codon)
    return gene

def linear_contains(gene, key_codon):
    for codon in gene:
        if codon == key_codon:
            return True
    return False

def binary_contains(gene, key_codon):
    low = 0
    high = len(gene) - 1
    while low <= high:
        mid = (low + high) // 2
        if gene[mid] < key_codon:
            low = mid + 1
        elif gene[mid] > key_codon:
            high = mid - 1
        else:
            return True
    return False

# Data Preparation
my_gene = string_to_gene(gene_str)
sorted_gene = sorted(my_gene)

# Codons to Search
acg = (Nucleotide.A, Nucleotide.C, Nucleotide.G)
gat = (Nucleotide.G, Nucleotide.A, Nucleotide.T)
cag = (Nucleotide.C, Nucleotide.A, Nucleotide.G)

# Linear Search
print(linear_contains(my_gene, acg))
print(linear_contains(my_gene, gat))
print(linear_contains(my_gene, cag))
print(f"linear_contains execution time for ACG >>>> {t.timeit(lambda: linear_contains(my_gene, acg), number=1000)}")
print(f"linear_contains execution time for GAT >>>> {t.timeit(lambda: linear_contains(my_gene, gat), number=1000)}")
print(f"linear_contains execution time for CAG >>>> {t.timeit(lambda: linear_contains(my_gene, cag), number=1000)}")

# Binary Search
print(binary_contains(sorted_gene, acg))
print(binary_contains(sorted_gene, gat))
print(binary_contains(sorted_gene, cag))

print(f"binary_contains execution time for ACG >>>> {t.timeit(lambda: binary_contains(sorted_gene, acg), number=1000)}")
print(f"binary_contains execution time for GAT >>>> {t.timeit(lambda: binary_contains(sorted_gene, gat), number=1000)}")
print(f"binary_contains execution time for CAG >>>> {t.timeit(lambda: binary_contains(sorted_gene, cag), number=1000)}")