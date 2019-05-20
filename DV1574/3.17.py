def list_to_dict(vector):
    vector_dict = {}
    for a in range(0, len(vector)):
        if vector[a] != 0:
            vector_dict[a] = vector[a]
    return vector_dict

print(list_to_dict([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]))