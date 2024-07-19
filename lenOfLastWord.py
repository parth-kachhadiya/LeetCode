def lenOfLastWord(s):
    ctr = 0
    for i in range(len(s)-1,-1,-1):
        if s[i] != ' ':
            ctr += 1
        else:
            if ctr > 0:
                return ctr
    return ctr

print(lenOfLastWord("Hello ParthKachhadiya"))