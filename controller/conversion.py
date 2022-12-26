
from controller.befGrammar import dct, startSymbol, display
varLS = ['A', 'B', 'C', 'D', 'E', 'F', 'V', 'Q', 'R', 'T', 'U']    # new variabel LeftSide
newRS = []  # inisiasi RS (RightSide)/ terminal baru
newLS = []  # inisiasi LS (LeftSide)/ variabel baru

# meminta konversion
def getconversion():    
    
    firstStep()      # menghilangkan Unit Production
    
    '''
        meminimalisir agar jumlah RS Terminal == 1
        serta agar jumlah RS Non-Terimal == 2, disamping itu
        menambah variable untuk tujuan konversi CNF
    '''
    secondStep()
    
    return dct


def firstStep():
    key = list(dct.keys()) # menyimpan semua LHS ke dalam key

    for i in key:
        for j in key:
            if i in dct[j]:
                dct[j].remove(i)    # menghapus Production I 
                dct[j].extend(dct[i])   # menambahkan RHS dari Production I

def secondStep():
    # ketika masih terdapat nilai yang lebih panjangnya lebih dari 2 :
    while(maxLen() > 2):
        for j in dct[startSymbol]:
            # ketika semua variabel dan panjang == 2 akan di continue                
            if len(j.split(' ')) <= 2: continue
            else: removeNonTerminal(startSymbol, j)        

def removeNonTerminal(nowKey, checkValue):
    lstCheckVal = checkValue.split(' ')
    newPrd = ''
    idx = getSubsIndex(newRS, checkValue)  # mencari indeks substring
    if idx == -1:   # jika tidak ada dalam var baru
        addVal = ' '.join(lstCheckVal[0:2])
        newLS.append(varLS[len(newLS)])
        newRS.append(addVal)
        newPrd = checkValue.replace(addVal, newLS[len(newLS)-1])
        dct.update({newLS[len(newLS)-1]: [addVal]})

    else: newPrd = checkValue.replace(newRS[idx], newLS[idx])

    # pada bagian ini akan memasukan RHS dengan newPrd
    dct[nowKey][dct[nowKey].index(checkValue)] = newPrd


def maxLen():
    maks = 0
    for i in dct[startSymbol]:
        if len(i.split(' ')) > maks: maks = len(i.split(' '))
    return maks


def getSubsIndex(newRS, checkString):
    for i in newRS:
        # jika terdapat i akan mengembalikan indexnya
        if i in checkString: return newRS.index(i)
    return -1

