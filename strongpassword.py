def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    a = 0
    has_number = False
    has_lower = False
    has_upper = False
    has_special = False

    for i in password:
        if i in numbers:
            has_number = True
        elif i in upper_case:
            has_upper = True
        elif i in lower_case:
            has_lower = True
        elif i in special_characters:
            has_special = True

    if not has_number:
        a += 1
    if not has_lower:
        a += 1
    if not has_upper:
        a += 1
    if not has_special:
        a += 1

    if n + a < 6:
        a += 6 - (n + a)

    return a

if __name__ == '__main__':
    n = int(input().strip())
    password = input()
    print(minimumNumber(n, password))
