def solve(s):
    
    word=s.split()
    for i in range(len(word)):
        word[i]=word[i].capitalize()
    result=' '.join(word)
    return result