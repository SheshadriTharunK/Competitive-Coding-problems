def pangrams(s):
    if all(letter in s for letter in lower):
        print('pangram')
    else:
        print("not pangram")

if __name__ == '__main__':
    s = input().lower().strip()
    lower = "abcdefghijklmnopqrstuvwxyz"
    pangrams(s)
