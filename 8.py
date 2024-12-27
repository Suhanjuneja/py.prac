# WAP to create a list of the cubes of only the even integers appearing in the input list using a 'for' loop

def cubes_of_even_numbers_loop(lst):
    result = []
    for x in lst:
        if x % 2 == 0:
            result.append(x**3)
    print(result)

cubes_of_even_numbers_loop([1, 2, 3, 4, 5, 6])

# WAP to create a list of cubes of only even integers from an input list using list comprehension

def cubes_of_even_numbers_comprehension(lst):
    print([x**3 for x in lst if isinstance(x, int) and x % 2 == 0])

cubes_of_even_numbers_comprehension([1, 2, 3, 4, 5, 6])
