import re

def count_atoms(formula):
    # Regular expression to match elements and their counts
    pattern = r'([A-Z][a-z]*)(\d*)'
    elements = re.findall(pattern, formula)

    # Dictionary to store counts of each element
    atom_counts = {'C': 0, 'H': 0, 'O': 0}

    # Loop through matched elements and update counts
    for element, count in elements:
        count = int(count) if count else 1
        atom_counts[element] += count

    return atom_counts

def main():
    formula = input("Введите формулу в формате SMILE: ")
    atom_counts = count_atoms(formula)
    print("Количество атомов каждого элемента:")
    for element, count in atom_counts.items():
        print(f"{element}: {count}")

if __name__ == "__main__":
    main()