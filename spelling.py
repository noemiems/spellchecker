import re
stringa = "bonana chocuulate beaitufil boatt carr cardz pizza pianno energet thouh"
IN = open("words_alpha.txt")
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
    def addition(a,b):
        return dp[a][b-1]
    def remove(a,b):
        return dp[a-1][b]
    def replace(a,b):
        return dp[a-1][b-1]
    for i in range(m + 1):
        for j in range(n + 1):

            if i == 0:
                dp[i][j] = j

            elif j == 0:
                dp[i][j] = i

            elif str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = 1 + min(addition(i,j),
                                   remove(i,j),
                                   replace(i,j))

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

    if len(newlista) >= len(newlistb) :
        for y in range(len(newlista)):
            if len(newlistb) != 0:
                finalchar = newlista[-1]
                finalcharb = newlistb[-1]
                if finalchar != finalcharb:
                    if newlista[-2] == newlistb[-1]:
                        solution.append("Deletion")
                        newlista.pop(-1)
                    else:
                       solution.append("Substitution")
                newlista.pop(-1)
                newlistb.pop(-1)
            if len(newlistb) == 0:
                if len(newlista) != 0:
                    solution.append("Deletion")
                    newlista.pop(-1)

    if len(newlista) < len(newlistb) :
        for z in range(len(newlistb)):
            if len(newlista) != 0:
                finalchar = newlista[-1]
                finalcharb = newlistb[-1]
                if finalchar != finalcharb:
                    if newlistb[-2] == newlista[-1]:
                        solution.append("Insertion")
                        newlistb.pop(-1)
                    else:
                        solution.append("Substitution")
                newlista.pop(-1)
                newlistb.pop(-1)
            if len(newlista) == 0:
                if len(newlistb) != 0:
                    solution.append("Insertion")
                    newlistb.pop(-1)

    sumactions = len(solution)

    print('The best correction for', str1, 'is', good, '\n', 'The minimum number of operations is', sumactions,'\n','The operations are the following:', solution)
