#print("input yours combination (7 cards): ")
#c1 = input()
#c2 = input()
#c3 = input()
#c4 = input()
#c5 = input()
#c6 = input()
#c7 = input()
#h1 = [c1, c2, c3, c4, c5, c6, c7]
h1 = ["As", "3s", "5s", "4s", "Qc", "2s", "Ks"]
# finding royal-flush
RF = 0
RFd = [10, 11, 12, 13, 14]#first condition
HRF = ["10h", "Jh", "Qh", "Kh", "Ah"]
DRF = ["10d", "Jd", "Qd", "Kd", "Ad"]
CRF = ["10c", "Jc", "Qc", "Kc", "Ac"]
SRF = ["10s", "Js", "Qs", "Ks", "As"]
r1H = len(list(set(h1) & set(HRF)))
if r1H >= 5:
    RF = 1
r1D = len(list(set(h1) & set(DRF)))
if r1D >= 5:
    RF = 1
r1C = len(list(set(h1) & set(CRF)))
if r1C >= 5:
    RF = 1
r1S = len(list(set(h1) & set(SRF)))
if r1S >= 5:
    RF = 1
#finding straight-flush
#hearts
HS1 = ["2h", "3h", "4h", "5h", "6h"]
rH = len(list(set(h1) & set(HS1)))
if rH >= 5:
    SF = 1
    sSF = 20
HS2 = ["3h", "4h", "5h", "6h", "7h"]
rH = len(list(set(h1) & set(HS2)))
if rH >= 5:
    SF = 1
    sSF = 25
HS3 = ["4h", "5h", "6h", "7h", "8h"]
rH = len(list(set(h1) & set(HS3)))
if rH >= 5:
    SF = 1
    sSF = 30
HS4 = ["5h", "6h", "7h", "8h", "9h"]
rH = len(list(set(h1) & set(HS4)))
if rH >= 5:
    SF = 1
    sSF = 35
HS5 = ["6h", "7h", "8h", "9h", "10h"]
rH = len(list(set(h1) & set(HS5)))
if rH >= 5:
    SF = 1
    sSF = 40
HS6 = ["7h", "8h", "9h", "10h", "Jh"]
rH = len(list(set(h1) & set(HS6)))
if rH >= 5:
    SF = 1
    sSF = 45
HS7 = ["8h", "9h", "10h", "Jh", "Qh"]
rH = len(list(set(h1) & set(HS7)))
if rH >= 5:
    SF = 1
    sSF = 50
HS8 = ["9h", "10h", "Jh", "Qh", "Kh"]
rH = len(list(set(h1) & set(HS8)))
if rH >= 5:
    SF = 1
    sSF = 55
HS9 = ["2h", "3h", "4h", "5h", "Ah"]
rH = len(list(set(h1) & set(HS9)))
if rH >= 5:
    SF = 1
    sSF = 15
#D
DS1 = ["2d", "3d", "4d", "5d", "6d"]
rD = len(list(set(h1) & set(DS1)))
if rD >= 5:
    SF = 1
    sSF = 20
DS2 = ["3d", "4d", "5d", "6d", "7d"]
rD = len(list(set(h1) & set(DS2)))
if rD >= 5:
    SF = 1
    sSF = 25
DS3 = ["4d", "5d", "6d", "7d", "8d"]
rD = len(list(set(h1) & set(DS3)))
if rD >= 5:
    SF = 1
    sSF = 30
DS4 = ["5d", "6d", "7d", "8d", "9d"]
rD = len(list(set(h1) & set(DS4)))
if rD >= 5:
    SF = 1
    sSF = 35
DS5 = ["6d", "7d", "8d", "9d", "10d"]
rD = len(list(set(h1) & set(DS5)))
if rD >= 5:
    SF = 1
    sSF = 40
DS6 = ["7d", "8d", "9d", "10d", "Jd"]
rD = len(list(set(h1) & set(DS6)))
if rD >= 5:
    SF = 1
    sSF = 45
DS7 = ["8d", "9d", "10d", "Jd", "Qd"]
rD = len(list(set(h1) & set(DS7)))
if rD >= 5:
    SF = 1
    sSF = 50
DS8 = ["9d", "10d", "Jd", "Qd", "Kd"]
rD = len(list(set(h1) & set(DS8)))
if rD >= 5:
    SF = 1
    sSF = 55
DS9 = ["2d", "3d", "4d", "5d", "Ad"]
rD = len(list(set(h1) & set(DS9)))
if rD >= 5:
    SF = 1
    sSF = 15
#C
CS1 = ["2c", "3c", "4c", "5c", "6c"]
rC = len(list(set(h1) & set(CS1)))
if rC >= 5:
    SF = 1
    sSF = 20
CS2 = ["3c", "4c", "5c", "6c", "7c"]
rC = len(list(set(h1) & set(CS2)))
if rC >= 5:
    SF = 1
    sSF = 25
CS3 = ["4c", "5c", "6c", "7c", "8c"]
rC = len(list(set(h1) & set(CS3)))
if rC >= 5:
    SF = 1
    sSF = 30
CS4 = ["5c", "6c", "7c", "8c", "9c"]
rC = len(list(set(h1) & set(CS4)))
if rC >= 5:
    SF = 1
    sSF = 35
CS5 = ["6c", "7c", "8c", "9c", "10c"]
rC = len(list(set(h1) & set(CS5)))
if rC >= 5:
    SF = 1
    sSF = 40
CS6 = ["7c", "8c", "9c", "10c", "Jc"]
rC = len(list(set(h1) & set(CS6)))
if rC >= 5:
    SF = 1
    sSF = 45
CS7 = ["8c", "9c", "10c", "Jc", "Qc"]
rC = len(list(set(h1) & set(CS7)))
if rC >= 5:
    SF = 1
    sSF = 50
CS8 = ["9c", "10c", "Jc", "Qc", "Kc"]
rC = len(list(set(h1) & set(CS8)))
if rC >= 5:
    SF = 1
    sSF = 55
CS9 = ["2c", "3c", "4c", "5c", "Ac"]
rC = len(list(set(h1) & set(CS9)))
if rC >= 5:
    SF = 1
    sSF = 15
#S
SS1 = ["2s", "3s", "4s", "5s", "6s"]
rS = len(list(set(h1) & set(SS1)))
if rS >= 5:
    SF = 1
    sSF = 20
SS2 = ["3s", "4s", "5s", "6s", "7s"]
rS = len(list(set(h1) & set(SS2)))
if rS >= 5:
    SF = 1
    sSF = 25
SS3 = ["4s", "5s", "6s", "7s", "8s"]
rS= len(list(set(h1) & set(SS3)))
if rS >= 5:
    SF = 1
    sSF = 30
SS4 = ["5s", "6s", "7s", "8s", "9s"]
rS = len(list(set(h1) & set(SS4)))
if rS >= 5:
    SF = 1
    sSF = 35
SS5 = ["6s", "7s", "8s", "9s", "10s"]
rS = len(list(set(h1) & set(SS5)))
if rS >= 5:
    SF = 1
    sSF = 40
SS6 = ["7s", "8s", "9s", "10s", "Js"]
rS = len(list(set(h1) & set(SS6)))
if rS >= 5:
    SF = 1
    sSF = 45
SS7 = ["8s", "9s", "10s", "Js", "Qs"]
rS = len(list(set(h1) & set(SS7)))
if rS >= 5:
    SF = 1
    sSF = 50
SS8 = ["9s", "10s", "Js", "Qs", "Ks"]
rS = len(list(set(h1) & set(SS8)))
if rS >= 5:
    SF = 1
    sSF = 55
SS9 = ["2s", "3s", "4s", "5s", "As"]
rS = len(list(set(h1) & set(SS9)))
if rS >= 5:
    SF = 1
    sSF = 15
# finding pairs, two pairs, triple, full house, quads
#repeats = []
#repeats.insert(2, hand1digits.count(2))
#repeats.insert(3, hand1digits.count(3))
#repeats.insert(4, hand1digits.count(4))
#repeats.insert(5, hand1digits.count(5))
#repeats.insert(6, hand1digits.count(6))
#repeats.insert(7, hand1digits.count(7))
#repeats.insert(8, hand1digits.count(8))
#repeats.insert(9, hand1digits.count(9))
#repeats.insert(10, hand1digits.count(10))
#repeats.insert(11, hand1digits.count(11))
#repeats.insert(12, hand1digits.count(12))
#repeats.insert(13, hand1digits.count(13))
#repeats.insert(14, hand1digits.count(14))
#a = max(repeats)
#b = repeats.index(max(repeats)) + 2
#print(repeats)
#for i in repeats:
    #if i == 4:
        #sQ = (repeats.index(i) + 2)*4
        #print("quads")
    #if i == 3:
        #sT = (repeats.index(i) + 2)*3
        #print("triple")

