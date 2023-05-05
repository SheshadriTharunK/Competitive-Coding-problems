T = int(input())
for i in range(T):
    s = input()
    output = ""
    a = 0
    while a < len(s):
        char = s[a]
        count = 0
        a += 1
        while a < len(s) and s[a].isdigit():
            count = count * 10 + int(s[a])
            a += 1
        output += char*count
    print("Case {}: {}".format(i+1, output))
