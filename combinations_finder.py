#print("input yours combination (7 cards): ")
#c1 = input()
#c2 = input()
#c3 = input()
#c4 = input()
#c5 = input()
#c6 = input()
#c7 = input()
#h1 = [c1, c2, c3, c4, c5, c6, c7]
h1 = ["7h", "7s", "7d", "5c", "Qc", "2s", "Ks"]
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
SF = 0
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
#finding quads
Q = 0
Q2 = ["2h", "2d", "2c", "2s"]
q2 = len(list(set(h1) & set(Q2)))
if q2 >= 4:
    Q = 1
    sQ = 8
Q3 = ["3h", "3d", "3c", "3s"]
q3 = len(list(set(h1) & set(Q3)))
if q3 >= 4:
    Q = 1
    sQ = 12
Q4 = ["4h", "4d", "4c", "4s"]
q4 = len(list(set(h1) & set(Q4)))
if q4 >= 4:
    Q = 1
    sQ = 16
Q5 = ["5h", "5d", "5c", "5s"]
q5 = len(list(set(h1) & set(Q5)))
if q5 >= 4:
    Q = 1
    sQ = 20
Q6 = ["6h", "6d", "6c", "6s"]
q6 = len(list(set(h1) & set(Q6)))
if q6 >= 4:
    Q = 1
    sQ = 24
Q7 = ["7h", "7d", "7c", "7s"]
q7 = len(list(set(h1) & set(Q7)))
if q7 >= 4:
    Q = 1
    sQ = 28
Q8 = ["8h", "8d", "8c", "8s"]
q8 = len(list(set(h1) & set(Q8)))
if q8 >= 4:
    Q = 1
    sQ = 32
Q9 = ["9h", "9d", "9c", "9s"]
q9 = len(list(set(h1) & set(Q9)))
if q9 >= 4:
    Q = 1
    sQ = 36
Q10 = ["10h", "10d", "10c", "10s"]
q10 = len(list(set(h1) & set(Q10)))
if q10 >= 4:
    Q = 1
    sQ = 40
Q11 = ["Jh", "Jd", "Jc", "Js"]
q11 = len(list(set(h1) & set(Q11)))
if q11 >= 4:
    Q = 1
    sQ = 44
Q12 = ["Qh", "Qd", "Qc", "Qs"]
q12 = len(list(set(h1) & set(Q12)))
if q12 >= 4:
    Q = 1
    sQ = 48
Q13 = ["Kh", "Kd", "Kc", "Ks"]
q13 = len(list(set(h1) & set(Q13)))
if q13 >= 4:
    Q = 1
    sQ = 52
Q14= ["Ah", "Ad", "Ac", "As"]
q14 = len(list(set(h1) & set(Q14)))
if q14 >= 4:
    Q = 1
    sQ = 56
#finding triple
T = 0
h1 = [7,4,3,2,6,6,14]
repeats3 = []
repeats3.insert(2, h1.count(2))
repeats3.insert(3, h1.count(3))
repeats3.insert(4, h1.count(4))
repeats3.insert(5, h1.count(5))
repeats3.insert(6, h1.count(6))
repeats3.insert(7, h1.count(7))
repeats3.insert(8, h1.count(8))
repeats3.insert(9, h1.count(9))
repeats3.insert(10, h1.count(10))
repeats3.insert(11, h1.count(11))
repeats3.insert(12, h1.count(12))
repeats3.insert(13, h1.count(13))
repeats3.insert(14, h1.count(14))
a = max(repeats3)
b = repeats3.index(max(repeats3)) + 2
for i in repeats3:
        if i == 3:
            T = 1
            sT = b * 3
#finding two pairs
P = 0
TP = 0
repeats22 = []
repeats22.insert(2, h1.count(2))
repeats22.insert(3, h1.count(3))
repeats22.insert(4, h1.count(4))
repeats22.insert(5, h1.count(5))
repeats22.insert(6, h1.count(6))
repeats22.insert(7, h1.count(7))
repeats22.insert(8, h1.count(8))
repeats22.insert(9, h1.count(9))
repeats22.insert(10, h1.count(10))
repeats22.insert(11, h1.count(11))
repeats22.insert(12, h1.count(12))
repeats22.insert(13, h1.count(13))
repeats22.insert(14, h1.count(14))
a22 = repeats22.count(2)
if a22 == 2:
    TP = 1
    sTP = 0
if a22 == 1:
    P = 1
    sP = (repeats22.index(2)+2) * 2

#finding high card
H = 0
h = max(h1)
#summary listing!
summary = [RF, SF, Q, T, P, H]
