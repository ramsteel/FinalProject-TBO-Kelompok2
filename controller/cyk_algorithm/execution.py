
import copy # import modul table dan lib copy
import streamlit as st

dct = {}
kalPattern = ['S P', 'S P O', 'S P O Ket', 'S P Ket', 'S P Pel Ket', 'S P Pel']
verbPel = ['bermain', 'belajar', 'berisi', 'bercucuran', 'bermandikan', 'berpegangan', 'berjatuhan', 'berlatih']


def exec(newDct, fillTable, lstInput):
    cnt = 0
    global dct
    dct = newDct
    strTable = copy.deepcopy(fillTable) # copy tabel fillTable dijadikan ke dalam bentuk string

    for x in range(len(lstInput)):
        i = 0   # inisiasi i = 0
        for j in range(x,len(lstInput)):
            # ketika tabel masih kosong langsung memanggil checkProduction()
            if x == 0: fillTable[i][j] = checkProduction([lstInput[j]])
            else:   # jika sudah terisi pada bagian awal, maka
                res = []    # deklarasi res dengan list kosong
                for k in range(x):  # tiap putaran k akan memanggil fungsi union
                    union(res, fillTable[i][i+k], fillTable[i+(k+1)][j])
                fillTable[i][j] = checkProduction(res)  # hasil union akan dicek ke dalam checkProduction()
            if fillTable[i][j] == {'Ø'} and cnt == 0:
                print('Maaf terdapat kata yang tidak sesuai pada grammar')
                return lstInput[j], -1 
            strTable[i][j] = str(fillTable[i][j])   # mengconvert ke dalam list untuk masalah cetak tabel
            i+=1 # menjumlahkan i dengan satu ketika tabel akan bergerak vertikal
        cnt+=1
    
    return strTable, isAccepted(fillTable) # mengecek apakah string diterima atau tidak

def union(res, x, y):   # konkatenasi dan union dari string
    for i in x:
        for j in y:
            # ketika tabel berisi himpunan kosong, maka akan langsung dilanjutkan
            if i == set() or j == set() : continue
            res.append(i+' '+j) # konkatenasi antar nilai dalam set


def checkProduction(res):   # melakukan cek irisan terhadap production yang ada
    valTable = set()    # deklarasi set kosong
    for key in list(dct.keys()):
        # ketika terdapat irisan antara set hasil union dengan set Production
        if set.intersection(set(res), set(dct[key])) != set():
            valTable.add(key)   # menambahkan LHS ke dalam set kosong  
    if valTable == set(): valTable.add('Ø')
    return valTable 

def isAccepted(fillTable):
    print('\nHasil : ', end='')
    # ketika start production berada dalam puncak tabel filling maka,
    if list(dct.keys())[0] in fillTable[0][len(fillTable)-1]: 
        print('Kalimat Valid\n') #string diterima
        st.write(':green[_Kalimat Valid_]')
        return True
    else: 
        print('Kalimat Tidak Valid\n') #jika tidak string ditolak
        st.write(':red[_Kalimat Tidak Valid_]')
        return False
