import re
from rdkit import Chem

def smiles_to_inchi(smiles_formula):
    # Условия для поиска хим формулы
    patternSearch = r'InChI=1S/([A-Za-z0-9+]+)'
    # Перевод SMILES в Inchi формат
    mol = Chem.MolFromSmiles(smiles_formula)
    if mol is None:
        return "Неверный SMILES"
    inchi = Chem.MolToInchi(mol)
    # Вычленение хим формулы
    match = re.search(patternSearch, inchi)
    if match:
        formula_string = match.group(1)
        print(formula_string)
    else:
        return "Форула не обнаружена"
    pattern = r'(\d*)([A-Z][a-z]*)(\d*)'
    elements = re.findall(pattern, formula_string)
    # Массив для подсчета
    atom_counts = {}
    # Поиск элементов и подсчет
    for prefix, element, count in elements:
        prefix = int(prefix) if prefix else 1
        count = int(count) if count else 1
        if element in atom_counts:
            atom_counts[element] += count 
        else:
            atom_counts[element] = count * prefix 
    return atom_counts
def main():
    formula = input("Введите формулу в формате SMILE: ")
    element_counts = smiles_to_inchi(formula)
    print(element_counts)
if __name__ == "__main__":
    main()