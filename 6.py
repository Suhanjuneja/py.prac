# WAP to swap the first n characters of two strings

def swap_first_n(str1, str2, n):
    if n > len(str1) or n > len(str2):
        return "n is too large"
    new_str1 = str2[:n] + str1[n:]
    new_str2 = str1[:n] + str2[n:]
    return new_str1, new_str2

result = swap_first_n("hello", "world", 2)
print(result) 
