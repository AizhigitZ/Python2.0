def check_bigger(a, b):
    if a > b:
        return "a is bigger"
    elif b > a:
        return "b is bigger"
    else:
        return "they are equal"
    

a, b = map(int, input("Enter a and b with the space between them: ").split())
    

print(check_bigger(a, b))