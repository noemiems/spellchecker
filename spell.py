import re
stringa = "bonana chocuulate beaitufil boatt carr cardz pizza pianno energet thouh"
IN = open("words_alpha.txt")
line = 'XXX'
wordlist = []
text = []
good = []

stringb = re.split(' ', stringa)

while line:
    line = IN.readline()
    line.strip()
    text.append(line[:-1])

for x in stringb:
    if x != None:
        wordlist.append(x)


def editDistDP(str1, str2, m, n):

    dp = [[0 for x in range(n + 1)] for x in range(m + 1)] #Starting the matrix?
    def addition(a,b):
        return dp[a][b-1]
    def remove(a,b):
        return dp[a-1][b]
    def replace(a,b):
        return dp[a-1][b-1]
    for i in range(m + 1): #length word +1 for the extra row
        for j in range(n + 1): #length word +1 for the extra column

            if i == 0: #if words are not the same length
                dp[i][j] = j

            elif j == 0: #if words are not the same length
                dp[i][j] = i

            elif str1[i-1] == str2[j-1]: #If letters are the same
                dp[i][j] = dp[i-1][j-1]

            else:
                def stats(iterable):
                    it = iter(iterable)
                    first = next(it)
                    minimum = maximum = cumsum = first
                    n = 1
                    for x in it:
                        n += 1
                        cumsum += x
                        if x < minimum:
                            minimum = x
                            return minimum
                dp[i][j] = 1 + min(addition(i,j),        # Insert
                                   remove(i,j),        # Remove
                                   replace(i,j))    # Replace

    return dp[m][n]

for word in range(len(wordlist)):
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
            print(str1, good)
            print('The minimum number of operations was:', sortdict[0][1])
            break
