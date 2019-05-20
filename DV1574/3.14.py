def base_composition(compostion):
    comp_dict = {"A": 0, "C": 0, "T": 0, "G": 0}

    for a in compostion:
        comp_dict[a] += 1
    return comp_dict

print(base_composition("CTATCGGCACCCTTTCAGCA"))