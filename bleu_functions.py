def tokenize(dictionary):
    """converts a dictionary of texts to a list of lists of tokens"""
    returned_list = []
    for key, value in dictionary.items():
        list_val = value.split()
        returned_list.append(list_val)
    return returned_list