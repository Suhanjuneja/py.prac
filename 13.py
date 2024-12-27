def NameChecker():
    name=input("Enter a name without any spaces:")
    if name.isalpha():
        print(name,"is a good name")
    else:
        raise Exception("Only alphabetic characters are allowed for name.")
NameChecker()
