#function that print the dict. where keys are nos.

def generate_cubes_dict():
    cubes_dict = {}
    for i in range(1, 6):
        cubes_dict[i] = i ** 3
    print(cubes_dict)
generate_cubes_dict()
