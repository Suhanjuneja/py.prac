def tuple_operations():
    t1 = (1, 2, 5, 7, 9, 2, 4, 6, 8, 10)
    t2 = (11, 13, 15)

    # (a) Print half the values of the tuple in one line and the other half in the next line.
    mid = len(t1) // 2
    first_half = t1[:mid]
    second_half = t1[mid:]
    print("First half:", first_half)
    print("Second half:", second_half)

    # (b) Print another tuple whose values are even numbers in the given tuple.
    even_numbers = ()
    for num in t1:  
        if num % 2 == 0:
            even_numbers += (num,)
    print("Even numbers:", even_numbers)

    # (c) Concatenate tuple t1 with t2.
    concatenated_tuple = t1 + t2
    print("Concatenated tuple:", concatenated_tuple)

    # (d) Return maximum and minimum values from the tuple.
    
    print("Maximum value:", max(concatenated_tuple))
    print("Minimum value:", min(concatenated_tuple))
tuple_operations()
