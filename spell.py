import re
stringa = "bonana chocuulate beaitufil boatt carr cardz pizza pianno energet thouh"
IN = open("dictionary.txt")
line = 'XXX'
wordlist = []
good = []
solution = []
newlista = []
newlistb = []
text = []

stringb = re.split(' ', stringa)

while line:
    line = IN.readline()
    line.strip()
    text.append(line[:-1])

for x in stringb:
    if x != None:
        wordlist.append(x)

def editDistDP(str1, str2, m, n):

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)]
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(dp[i][j-1],
                                   dp[i-1][j],
                                   dp[i-1][j-1])

    return dp[m][n]

def alphalist(a,b):
    for x in range(len(a)):
        for y in range(len(a[x])):
            b.append(a[x])

for word in range(len(wordlist)):
    solution = []
    if wordlist[word] not in text:
        dict = {}
        str1 = wordlist[word]
        for x in range(len(text)):
            str2 = text[x]
            operationsnum = editDistDP(str1, str2, len(str1), len(str2))
            if operationsnum <= 4:
                dict[str2] = operationsnum
                sortdict = sorted(dict.items(), key=lambda x:x[1])
        for item in range(len(sortdict)):
            good = sortdict[0][0]

    alphalist(str1, newlista)
    alphalist(good, newlistb)

    def something(a, b, c, d):
        if len(a) >= len(b) :
            for y in range(len(a)):
                if len(b) != 0:
                    finalchar = a[-1]
                    finalcharb = b[-1]
                    if finalchar != finalcharb:
                        if a[-2] == b[-1]:
                            c.append(d)
                            a.pop(-1)
                        else:
                            c.append("Substitution")
                    a.pop(-1)
                    b.pop(-1)
                if len(b) == 0:
                    if len(a) != 0:
                        c.append(d)
                        a.pop(-1)
    something(newlista, newlistb, solution, "Deletion")
    something(newlistb, newlista, solution, "Insertion")

    sumactions = len(solution)

    print('The best correction for', str1, 'is', good, '\n', 'The Levenshtein distance is', sumactions,'\n','The operations are the following:', solution)
