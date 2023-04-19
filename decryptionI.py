s=input()
n=int(input())
plain=''
for i in s:
    if i.islower():
        plain+=chr((ord(i)-n-97)%26+97)
    elif i.isupper():
        plain+=chr((ord(i)-n-65)%26+65)
    elif i==' ':
        plain+=i
    elif i in "0123456789":
        plain+=i
print(plain)