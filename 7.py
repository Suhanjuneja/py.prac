# WAP to return indices of all occurrences of the second string in the first string

def find_substring_indices(main_str, sub_str):
    indices = []
    i = main_str.find(sub_str)
    while i != -1:
        indices.append(i)
        i = main_str.find(sub_str, i + 1)
    if indices:
      print(indices)
    else:
      print("-1")

find_substring_indices("hello hello", "lo")
find_substring_indices("hello world", "xyz")
