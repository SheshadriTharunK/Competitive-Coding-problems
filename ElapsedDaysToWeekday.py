days=int(input())
dict1={1:'Saturday',2:'Sunday',3:'Monday',4:'Tuesday',5:'Wednesday',6:'Thursday',7:'Friday'}
week=days%7+1 
print(dict1[week])
