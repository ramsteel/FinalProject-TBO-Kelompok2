
# mencari string terpanjang
def getMaxLength(fillTable):
    maxLen = -1 # inisiasi panjang maksimal dengan -1
    for i in fillTable:
        temp = len(max(i,key=len))
        # ketika panjang dari string tiap nilai dari filltabel
        # lebih bersar dari maxlen maka maxLen akan = temp
        if temp>maxLen: maxLen = temp
    return maxLen

# mencetak tabel
def printTable(fillTable):
    print('\n==== Tabel Filling ====\n')
    maxLen = getMaxLength(fillTable) + 5 # panjang maks akan ditambah 5
    #bertujuan untuk memberikan space 

    for x in range(len(fillTable)):
        i = 0
        upperBound = (x+1)*(maxLen)*'-' + (x+2)*'-' # inisiasi upperbound
        print(upperBound)   # mencetak upperbound
        print(end='|')  # dengan batas = '|'
        for j in range((len(fillTable)-1)-x, len(fillTable)):
            # ketika value filltable kosong maka mencetak 'Ø'
            if fillTable[i][j] == 'set()': 
                fillTable[i][j] = 'Ø'
                print('Ø'.center(maxLen), end='|')
            # jika tidak akan mencetak nilainya dengan total length yang diambil = maxLen
            else: print(str(fillTable[i][j]).center(maxLen), end='|')
            i+=1
        print()
    print(len(fillTable)*(maxLen)*'-' + (len(fillTable)+1)*'-') # mencetak akhir filltable
