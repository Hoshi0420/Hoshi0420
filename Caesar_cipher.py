def encipher(p, k):
    c = ''
    for i in range(len(p)):
        a = ord(p[i])
        t = a + k
        c += chr(t)
    return c


Text = input("Input the word: ")
level = int(input("암호화 단계: "))

print("원문:" + Text)
print("암호화 :" + encipher(Text, level))
