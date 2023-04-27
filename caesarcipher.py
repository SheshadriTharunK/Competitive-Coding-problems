
def caesarCipher(s, k):
    message=''
    for i in s:
      if i.isupper():
        message+=chr((ord(i)+k-65)%26+65)
      elif i.islower():
        message+=chr((ord(i)+k-97)%26+97)
      else:
        message+=i
    print(message)
    
if __name__ == '__main__':
    
    n = int(input().strip())

    s = input()

    k = int(input().strip())

    result = caesarCipher(s, k)

